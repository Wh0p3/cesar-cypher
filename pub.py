#!/usr/bin/python3
import rospy
from std_msgs.msg import String
from std_msgs.msg import Char
rospy.init_node("publisher")
publisher=rospy.Publisher("/cesar",String,queue_size=10)
rate=rospy.Rate(1)
word="Adithya"
def encrypt(text,s=5):
    result = ""
   
    for i in text:
        strin=ord(i)+s
        result=result+chr(strin)

    return result


while not rospy.is_shutdown():
   newword=encrypt(word,5)
   publisher.publish(newword)
   rate.sleep()

   