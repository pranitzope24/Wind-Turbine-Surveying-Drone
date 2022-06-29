#!/usr/bin/env python

import rospy
import math
import time
from geometry_msgs.msg import TwistStamped
from rospy.topics import Publisher

def funct():
    rospy.init_node('square')
    pub=rospy.Publisher('/mavros/setpoint_velocity/cmd_vel', queue_size='10')
    rate=rospy.Rate(100)
    vel=TwistStamped()
    t= int(round(time.time()))

    while not rospy.is_shutdown() :
        vel.twist.linear.x=math.sin(t/3)
        vel.twist.linear.y=math.cos(t/3)
        #t=t+(math.pi)/180
        pub.publish(vel)
    
if __name__ == '__main__' :
    try :
        funct()
    except :
        rospy.ROSInterruptException
        pass

