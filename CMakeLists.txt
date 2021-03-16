cmake_minimum_required(VERSION 3.0.2)
project(ros_torch_libtorch)

find_package(catkin REQUIRED COMPONENTS 
  roscpp
  std_msgs
)
find_package(Torch REQUIRED)

catkin_package()

include_directories(include
${catkin_INCLUDE_DIRS}
)
message(STATUS "${catkin_INCLUDE_DIRS}")

add_executable(torch_publisher src/torch_publisher.cpp)

target_link_libraries(torch_publisher 
${TORCH_LIBRARIES}
${catkin_LIBRARIES}
)

set_property(TARGET torch_publisher PROPERTY CXX_STANDARD 14)
