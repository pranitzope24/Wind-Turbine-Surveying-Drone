#!/usr/bin/env python

import rospy
import math
import time
from geometry_msgs.msg import PoseStamped

#/mavros/local_position/pose
#/mavros/setpoint_position/local

cur_pos = PoseStamped()

def error():
    error=math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))
    return error

def publish():

def subscribe():

if __name__ =='__main__'
    