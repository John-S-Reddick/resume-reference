cmake_minimum_required(VERSION 3.21)
project(FourHulls)

set(CMAKE_PREFIX_PATH "/home/linuxbrew/.linuxbrew/Cellar/qt/6.2.2/lib/cmake/")

find_package(Qt6 COMPONENTS Widgets REQUIRED)

include_directories(/usr/local/include/)
include_directories(/home/linuxbrew/.linuxbrew/include/)
include_directories(/home/linuxbrew/.linuxbrew/Cellar/qt/6.2.2/include/)

link_directories(/usr/local/lib/)
link_directories(/home/linuxbrew/.linuxbrew/Cellar/)

set(CMAKE_CXX_FLAGS "-O3 -fopenmp -Wall -Wextra")
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_BUILD_TYPE "Debug")

add_executable(FourHulls main.cpp DrawUsingQt.h CGALComponents.h MyHeader.h GrahamScan.h JarvisMarch.h QuickHull.h ChansAlgorithim.h)

target_link_libraries(FourHulls Qt6::Core)
target_link_libraries(FourHulls Qt6::Widgets)
