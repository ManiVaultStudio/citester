cmake_minimum_required(VERSION 3.21)

project(CITester)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_EXTENSIONS OFF)

find_package(Poco REQUIRED)

add_executable(CITester src/timer.cpp)
target_link_libraries(CITester PRIVATE Poco::Poco)