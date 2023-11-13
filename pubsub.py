#!/usr/bin/python3
import rospy
from std_msgs.msg import String
rospy.init_node("decrypter")
def decrypt(message):
    message=message.data
    
    
    result = ""

    for letter in message:
            letterindex =ord(letter)
            letterindex=letterindex-5

            result = result + chr(letterindex)

        

    
    publish.publish(result)


subscriber=rospy.Subscriber("/cesar",String,decrypt)

publish=rospy.Publisher("/newtopic",String,queue_size=10)



while not rospy.is_shutdown():
    rospy.spin()
    
    