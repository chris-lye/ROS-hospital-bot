# ROS-hospital-bot

Turtlebot3 sim package is not included, but is a dependency required for simulations.
### Setup
Clone the TurtleBot3 Simulation Package
~~~~bash
cd src
git clone -b noetic-devel https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git
cd ..
catkin_make
~~~~
Install the packages required.
~~~~bash
sudo apt install ros-noetic-explore-lite
sudo apt-get install ros-noetic-navigation
~~~~
Source the environment setup for ROS before running catkin_make. 
~~~~bash
source /opt/ros/noetic/setup.bash
~~~~
### Instructions to run:
Make sure all turtlebot3 dependencies for Noetic here are installed:
https://emanual.robotis.com/docs/en/platform/turtlebot3/quick-start/ 

Install dependencies:
~~~~bash
sudo apt install ros-noetic-multirobot-map-merge ros-noetic-explore-lite
~~~~
#### Running on turtlebot:
On the remote launch the navigation module:
~~~~bash
roslaunch turtlebot3 roscore
# in another terminal, do
roslaunch turtlebot3 turtlebot3_navigation navigation_nomap.launch
~~~~
SSH into the robot and run:
~~~~bash
roslaunch turtlebot3_bringup turtlebot3_robot.launch
roslaunch auto_slam auto_slam.launch
~~~~
#### Running simulation:
~~~~bash
roslaunch turtlebot3_gazebo turtlebot3_stage_4.launch
~~~~
Then, open another terminal and run:
~~~~bash
roslaunch auto_slam auto_slam.launch
~~~~
After the auto SLAM is complete, to save the map, do:
~~~~bash
rosrun map_server map_saver -f /tmp/my_map
~~~~
### Other
#### How to compile custom python files
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
