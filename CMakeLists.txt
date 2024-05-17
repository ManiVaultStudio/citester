cmake_minimum_required(VERSION 3.21)

project(CITester)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_EXTENSIONS OFF)

find_package(fmt REQUIRED)

add_executable(CITester src/example.cpp)
target_link_libraries(CITester PRIVATE fmt::fmt)