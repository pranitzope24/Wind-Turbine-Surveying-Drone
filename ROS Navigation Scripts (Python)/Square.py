#!/usr/bin/env python

import rospy
import math
import time
from geometry_msgs.msg import PoseStamped

#/mavros/local_position/pose
#/mavros/setpoint_position/local

cur_pos = PoseStamped()

def error(x1,x2,y1,y2):
    error=math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))
    return error

def publish():
    rospy.init_node("Velocity_Node")
    pub_obj=rospy.Publisher("/mavros/setpoint_position/global",PoseStamped,queue_size=10)
    rate=rospy.Rate(50)
    dest1=PoseStamped()
    dest2=PoseStamped()
    dest3=PoseStamped()
    dest4=PoseStamped()
    dest1.pose.position.x=0
    dest1.pose.position.y=0
    dest1.pose.position.z=10
    dest2.pose.position.x=10
    dest2.pose.position.y=0
    dest2.pose.position.z=10
    dest3.pose.position.x=10
    dest3.pose.position.y=10
    dest3.pose.position.z=10
    dest4.pose.position.x=0
    dest4.pose.position.y=10
    dest4.pose.position.z=10
    while(error(cur_pos.pose.position.x,dest1.pose.position.x,cur_pos.pose.position.y,dest1.pose.position.y)>0.1):
        pub_obj.publish(dest1)
    while(error(cur_pos.pose.position.x,dest2.pose.position.x,cur_pos.pose.position.y,dest2.pose.position.y)>0.1):
        pub_obj.publish(dest2)
    while(error(cur_pos.pose.position.x,dest3.pose.position.x,cur_pos.pose.position.y,dest3.pose.position.y)>0.1):
        pub_obj.publish(dest3)
    while(error(cur_pos.pose.position.x,dest4.pose.position.x,cur_pos.pose.position.y,dest4.pose.position.y)>0.1):
        pub_obj.publish(dest4)
    
    
def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)



def subscribe():


if __name__ == '__main__':
    try:
        
    except rospy.ROSInterruptException:
        pass

    