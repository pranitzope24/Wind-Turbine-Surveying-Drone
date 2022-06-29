#!/usr/bin/env python

import rospy
import math
import time
from geometry_msgs.msg import PoseStamped

#/mavros/local_position/pose
#/mavros/setpoint_position/local
# lol.pose.position.x 
cur_pos = PoseStamped()

def error(x1,x2,y1,y2):
    error=math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))
    return error

def publish():
    rospy.init_node('square')
    pub=rospy.Publisher('#/mavros/setpoint_position/local',PoseStamped,queue_size='10')
    rate=rospy.Rate=100
    dest1 = PoseStamped()
    dest1.pose.position.x=10
    dest1.pose.position.y=0
    dest2 = PoseStamped()
    dest2.pose.position.x=10
    dest2.pose.position.y=10
    dest3 = PoseStamped()
    dest3.pose.position.x=0
    dest2.pose.position.y=10
    dest4 = PoseStamped()
    dest4.pose.position.x=0
    dest4.pose.position.y=0
    


def subscribe():

if __name__ =='__main__'