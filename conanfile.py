from conan import ConanFile
from conan.tools.files import copy
from conan.tools.cmake import CMake, CMakeToolchain, CMakeDeps

from pathlib import Path
import os
import re


class CITester(ConanFile):

    url = "https://github.com/ManiVaultStudio/citester"
    author = "B. van Lew b.van_lew@lumc.nl"  # conan recipe author
    license = "MIT"

    name = "citester"
    version = "1.0.0"
    description = """Test CI logic"""
    topics = ("ci test", "ManiVaultStudio")
    package_type = "application"

    settings = ("os", "build_type", "compiler", "arch")
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": True, "fPIC": True}
    exports_sources = "CMakeLists.txt", "src/*"

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def requirements(self):
        self.requires("fmt/11.1.4", options={"shared": True})
        self.requires("lz4/1.10.0", options={"shared": True})

    def generate(self):
        # These are the standard generators used in ManivaultStudio Plugins
        generator = None
        if self.settings.os == "Macos":
            generator = "Xcode"
        if self.settings.os == "Linux":
            generator = "Ninja Multi-Config"
        tc = CMakeToolchain(self, generator=generator)
        tc.variables["INSTALL_DIR"] = Path(self.build_folder, "install").as_posix()
        print(
            "Dependency fmt folders:  \n"
            "package_folder (equivalent to rootpath): \n"
            f"  {self.dependencies['lz4'].package_folder}\n"
            f"recipe_folder: {self.dependencies['lz4'].recipe_folder}\n"
            f"cpp_info:  {self.dependencies['lz4'].cpp_info}\n"
        )
        tc.generate()

        deps = CMakeDeps(self)
        deps.generate()

    def build(self):
        cmake = CMake(self)
        cmake.verbose = True
        cmake.configure()
        cmake.build(build_type="RelWithDebInfo")
        cmake.build(build_type="Release")

    def package(self):
        copy(self, pattern="Release/*", src=self.source_folder, dst=self.package_folder)
        copy(
            self,
            pattern="RelWithDebInfo/*",
            src=self.source_folder,
            dst=self.package_folder,
        )
