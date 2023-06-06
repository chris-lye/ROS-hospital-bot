#!/usr/bin/env python3
# Basics ROS program to publish real-time streaming 
# video from your built-in webcam
# Author:
# - Addison Sears-Collins
# - https://automaticaddison.com
 
# Import the necessary libraries
import rospy # Python library for ROS
from sensor_msgs.msg import Image # Image is the message type
from cv_bridge import CvBridge # Package to convert between ROS and OpenCV Images
import cv2 # OpenCV library
# from picamera.array import PiRGBArray
# from picamera import PiCamera
import datetime
  
def publish_message():
 
  # Node is publishing to the video_frames topic using 
  # the message type Image
  pub = rospy.Publisher('video_frames', Image, queue_size=10)
     
  # Tells rospy the name of the node.
  # Anonymous = True makes sure the node has a unique name. Random
  # numbers are added to the end of the name.
  rospy.init_node('video_pub_py', anonymous=True)
     
  # Go through the loop 10 times per second
  rate = rospy.Rate(10) # 10hz
     
  # Create a VideoCapture object
  # The argument '0' gets the default webcam.
  cap = cv2.VideoCapture()
  
  #camera = PiCamera()
  #camera.resolution = (640, 480)
  #camera.framerate = 32
  #rawCapture = PiRGBArray(camera, size=(640, 480))
  
  # allow the camera to warmup
  #time.sleep(0.1)
  
  # Used to convert between ROS and OpenCV images
  br = CvBridge()
 
  # While ROS is still running.
  while not rospy.is_shutdown():
     
      # Capture frame-by-frame
      # This method returns True/False as well
      # as the video frame.
      ret, frame = cap.read()      
         
      if ret == True:
        # Print debugging information to the terminal
        rospy.loginfo('publishing video frame')
             
        # Publish the image.
        # The 'cv2_to_imgmsg' method converts an OpenCV
        # image to a ROS image message
        pub.publish(br.cv2_to_imgmsg(frame))
        
        cv2.waitKey(5000) # wait for 5 seconds
        filename = "opencv_frame_{}.png".format(str(datetime.now()))
        cv2.imwrite(filename, frame)
        print("{} successfully saved!".format(filename))
        rospy.loginfo("{} successfully saved!".format(filename))
             
      # Sleep just enough to maintain the desired rate
      rate.sleep()
      
      # capture frames from the camera
      #for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	# grab the raw NumPy array representing the image, then initialize the timestamp and occupied/unoccupied text
	#image = frame.array # capture frames from the camera
	#if image:
	# Print debugging information to the terminal
         # rospy.loginfo('publishing video frame')
             
          # Publish the image.
          # The 'cv2_to_imgmsg' method converts an OpenCV
          # image to a ROS image message
         # pub.publish(br.cv2_to_imgmsg(image))
             
        # Sleep just enough to maintain the desired rate
       # rate.sleep()
        
	# clear the stream in preparation for the next frame
	# rawCapture.truncate(0)
	
         
if __name__ == '__main__':
  try:
    publish_message()
  except rospy.ROSInterruptException:
    pass
