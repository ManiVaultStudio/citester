cmake_minimum_required(VERSION 3.21)

project(CITester)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_EXTENSIONS OFF)

find_package(fmt REQUIRED)

add_executable(CITester src/example.cpp)
target_link_libraries(CITester PRIVATE fmt::fmt)

install(TARGETS CITester
    RUNTIME DESTINATION . COMPONENT CITESTER_EXECUTABLE
)   

add_custom_command(TARGET CITester POST_BUILD
	COMMAND "${CMAKE_COMMAND}"
	--install ${CMAKE_CURRENT_BINARY_DIR}
	--config $<CONFIGURATION>
	--prefix ${INSTALL_DIR}/$<CONFIGURATION>
)