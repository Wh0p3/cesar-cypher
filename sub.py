#!/usr/bin/python3
import rospy
from std_msgs.msg import String
rospy.init_node("printer")
def callback(message):
    print(message.data)
subscriber=rospy.Subscriber("/newtopic",String,callback)
while not rospy.is_shutdown():
    rospy.spin()