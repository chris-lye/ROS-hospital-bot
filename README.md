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
Make sure all turtlebot3 dependencies for Noetic here are installed:
https://emanual.robotis.com/docs/en/platform/turtlebot3/quick-start/ 

Install dependencies:
~~~~bash
sudo apt install ros-noetic-multirobot-map-merge ros-noetic-explore-lite
~~~~
#### Running on turtlebot:

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
