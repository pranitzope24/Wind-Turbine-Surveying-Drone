import rospy
import math
from gazebo_msgs.msg import LinkState
def func():
    rospy.init_node("Velocity_Node")
    pub_obj=rospy.Publisher("/gazebo/link_states",LinkState,queue_size=10)
    rate=rospy.Rate(10)
    velocity_msg=LinkState()
    while not rospy.is_shutdown():
        velocity_msg.twist.angular.y=5
        pub_obj.publish(velocity_msg)

if __name__ == '__main__':
    try:
        func()
    except rospy.ROSInterruptException:
        pass