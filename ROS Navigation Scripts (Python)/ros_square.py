#! /usr/bin/env python
import rospy
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import TwistStamped

current_pos = PoseStamped()
i = 0

a = []
b = []

def callback(msg):
  global current_pos
  current_pos = msg

def move():
 rospy.init_node('drone_square', anonymous=True)
 pub = rospy.Publisher('/mavros/setpoint_position/local', PoseStamped, queue_size=20)
 rospy.Subscriber('/mavros/local_position/pose', PoseStamped, callback)
 pos_msg = PoseStamped()
 
 j=1
 while j < 5 :
   print(j,"th vertex: ")
   a.append(float(input("enter x coordinate of ")))
   b.append(float(input("enter y coordinate of ")))
   j = j+1


 j=0
 r = rospy.Rate(20)
 while j<100:
   j = j+1
   setpoint_pub(pub,pos_msg,a[i],b[i])
   r.sleep()
 while(not rospy.is_shutdown()):

   xi = current_pos.pose.position.x
   yi = current_pos.pose.position.y
   wp_change(pub,pos_msg,xi,yi)
 

i = 0

def wp_change(pub,pos_msg,xi,yi):
  global i

  print("WP:",a[i],b[i])
  print("current :",xi,yi)
  dist = (a[i]-xi)**2 + (b[i]-yi)**2
  print("dist: ",dist)


  if dist < 0.5:
    i = i+1
    if i > 3:
      i=0
    setpoint_pub(pub,pos_msg,a[i],b[i])


def setpoint_pub(pub, pos_msg,a,b):
  pos_msg.pose.position.x = a
  pos_msg.pose.position.y = b
  pos_msg.pose.position.z = 10.0
  pos_msg.pose.orientation.x = 0
  pos_msg.pose.orientation.y = 0
  pos_msg.pose.orientation.z = 0
  pos_msg.pose.orientation.w = 1.0

  pub.publish(pos_msg)


if __name__ == "__main__":
  try :
    move()
  except rospy.ROSInterruptException:
     pass