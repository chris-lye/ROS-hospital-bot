#!/usr/bin/env python3
# Description:
# - Subscribes to real-time streaming video from your built-in webcam.
#
# Author:
# - Addison Sears-Collins
# - https://automaticaddison.com
 
# Import the necessary libraries
import rospy # Python library for ROS
from sensor_msgs.msg import Image # Image is the message type
from cv_bridge import CvBridge # Package to convert between ROS and OpenCV Images
import cv2 # OpenCV library
from datetime import datetime
 
def callback(data):
 
  # Used to convert between ROS and OpenCV images
  br = CvBridge()
 
  # Output debugging information to the terminal
  rospy.loginfo("receiving video frame")
   
  # Convert ROS Image message to OpenCV image
  current_frame = br.imgmsg_to_cv2(data)
   
  # Display image
  cv2.imshow("camera", current_frame)
   
  #k = 
  cv2.waitKey(5000) # wait for 5 seconds
  # click Space key to capture image (https://stackoverflow.com/questions/34588464/python-how-to-capture-image-from-webcam-on-click-using-opencv)
  # all other code is from: https://automaticaddison.com/working-with-ros-and-opencv-in-ros-noetic/
  #if k % 256 == 32:
  filename = "opencv_frame_{}.png".format(str(datetime.now()))
  cv2.imwrite(filename, current_frame)
  print("{} successfully saved!".format(filename))
  rospy.loginfo("{} successfully saved!".format(filename))
      
def receive_message():
 
  # Tells rospy the name of the node.
  # Anonymous = True makes sure the node has a unique name. Random
  # numbers are added to the end of the name. 
  rospy.init_node('video_sub_py', anonymous=True)
   
  # Node is subscribing to the video_frames topic
  rospy.Subscriber('video_frames', Image, callback)
 
  # spin() simply keeps python from exiting until this node is stopped
  rospy.spin()
 
  # Close down the video stream when done
  cv2.destroyAllWindows()
  
if __name__ == '__main__':
  receive_message()
