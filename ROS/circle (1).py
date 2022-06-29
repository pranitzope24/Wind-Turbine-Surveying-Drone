#!/usr/bin/env python

import rospy
import math
from geometry_msgs.msg import TwistStamped
from rospy.topics import Publisher

def funct():
    rospy.init_node('square')
    pub=rospy.Publisher('/mavros/setpoint_velocity/cmd_vel', queue_size='10')
    rate=rospy.Rate(10)
    vel=TwistStamped()
    t=0.0

    while not rospy.is_shutdown() :
        while (t<2*math.pi):
            vel.twist.linear.x=math.sin(t)
            vel.twist.linear.y=math.cos(t)
            t=t+(math.pi)/180
            pub.publish(vel)
        
if __name__ == '__main__' :
    try :
        funct()
    except :
        rospy.ROSInterruptException
    pass

