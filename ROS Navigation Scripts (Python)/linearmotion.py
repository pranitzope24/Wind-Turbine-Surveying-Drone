 #!/usr/bin/env python
import rospy
from geometry_msgs.msg import TwistStamped
def func():
    rospy.init_node("Velocity_Node")
    pub_obj=rospy.Publisher("/mavros/setpoint_velocity/cmd_vel",TwistStamped,queue_size=10)
    rate=rospy.Rate(10)
    velocity_msg=TwistStamped()
    velocity_msg.twist.linear.x=5
    velocity_msg.twist.linear.y=5
    while not rospy.is_shutdown():
        pub_obj.publish(velocity_msg)
if __name__ == '__main__':
    try:
        func()
    except rospy.ROSInterruptException:
        pass