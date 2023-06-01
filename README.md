# ROS-hospital-bot

Turtlebot3 sim package is not included, but is a dependency.
### Setup
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
### Instructions to run:

### How to compile custom python files
Whenever you create a new python file do
~~~bash
chmod +x new_file.py  
~~~
Then, to run the file
~~~bash
catkin_make
cd ~/catkin_ws  
source ./devel/setup.bash  
rosrun new_python_package new_file.py  
~~~
