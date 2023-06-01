# ROS-hospital-bot

Turtlebot3 sim package is not included, but is a dependency.

Clone the TurtleBot3 Simulation Package
~~~~bash
cd src
git clone -b noetic-devel https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git
cd ..
catkin_make
~~~~
Source the environment setup for ROS before running catkin_make. 
~~~~bash
source /opt/ros/noetic/setup.bash
~~~~
