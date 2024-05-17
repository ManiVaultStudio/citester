from conan import ConanFile
from conan.tools.files import copy
from conan.tools.cmake import CMake, CMakeToolchain, CMakeDeps

import os
import re

# Define compatibility fallbacks.
# These are dependencies where a different compiler version 
# from the can be substituted 
def compatibility(os, compiler, compiler_version):
    print(f"In citester compatibility function {os} {compiler} {compiler_version}")
    if os == "Macos" and compiler == "apple-clang" and bool(re.match("14.*", compiler_version)):  
        return """fmt/10.2.1:compiler.version=13
"""
    return None
class CITester(ConanFile):

    url = "https://github.com/ManiVaultStudio/citester"
    author = "B. van Lew b.van_lew@lumc.nl"  # conan recipe author
    license = "MIT"

    name = "citester"
    version = "1.0.0"
    description = """Test CI logic"""
    topics = ("ci test", "ManiVaultStudio")

    settings = {"os": None, "build_type": None, "compiler": None, "arch": None}
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": True, "fPIC": True}

    exports_sources = "CMakeLists.txt", "src/*"

    def requirements(self):
        self.requires("fmt/10.2.1")

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def generate(self):
        # These are the standard generators used in ManivaultStudio Plugins
        generator = None
        if self.settings.os == "Macos":
            generator = "Xcode"
        if self.settings.os == "Linux":
            generator = "Ninja Multi-Config"
        tc = CMakeToolchain(self, generator=generator)
        tc.generate()

        deps = CMakeDeps(self)
        deps.generate()

    def build(self):
        cmake = CMake(self)
        cmake.verbose = True
        cmake.configure()
        cmake.build()

    def package(self):
        copy(self, "*.h", os.path.join(self.source_folder, "include"), os.path.join(self.package_folder, "include"))
        copy(self, "*.a", os.path.join(self.build_folder, "build", "package_dep"), os.path.join(self.package_folder, "lib"), keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["package_dep"]