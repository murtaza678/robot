#!/usr/bin/env python

import rospy
import std_msgs.msg
from std_msgs.msg import Float64
from geometry_msgs.msg import Twist
from pynput import keyboard
def on_press(key):
	x='{0}'.format(key)
	if x== 'Key.up':
		msg = Twist()
		pub = rospy.Publisher('/mybot/cmd_vel',Twist,queue_size=5)
		pub_l= rospy.Publisher('/mybot/leftWheel_effort_controller/command',Float64,queue_size=5)
		pub_r= rospy.Publisher('/mybot/rightWheel_effort_controller/command',Float64,queue_size=5)
		msg.linear.x=2
		msg.linear.y=0
		msg.linear.z=0
		msg.angular.x=0
		msg.angular.y=0
		msg.angular.z=0
		#msg.speed=1
		pub_l.publish(0.0)
		pub_r.publish(0.0)
		pub.publish(msg)
	elif x== 'Key.down':
		msg = Twist()
		pub = rospy.Publisher('/mybot/cmd_vel',Twist,queue_size=5)
		pub_l= rospy.Publisher('/mybot/leftWheel_effort_controller/command',Float64,queue_size=5)
		pub_r = rospy.Publisher('/mybot/rightWheel_effort_controller/command',Float64,queue_size=5)
		pub_l.publish(0.0)
		pub_r.publish(0.0)
		msg.linear.x=-2
		msg.linear.y=0
		msg.linear.z=0
		msg.angular.x=0
		msg.angular.y=0
		msg.angular.z=0
		#msg.speed=1
		pub.publish(msg)

	elif x == 'Key.left':
		pub_l = rospy.Publisher('/mybot/leftWheel_effort_controller/command',Float64,queue_size=5)
		pub_r = rospy.Publisher('/mybot/rightWheel_effort_controller/command',Float64,queue_size=5)
		pub_l.publish(-15.0)
		pub_r.publish(15.0)

	elif x== 'Key.right':
		pub_l= rospy.Publisher('/mybot/leftWheel_effort_controller/command',Float64,queue_size=5)
		pub_r = rospy.Publisher('/mybot/rightWheel_effort_controller/command',Float64,queue_size=5)
		pub_l.publish(15.0)
		pub_r.publish(-15.0)



def on_release(key):
		msg = Twist()
		pub = rospy.Publisher('/mybot/cmd_vel',Twist,queue_size=5)
		msg.linear.x=0
		msg.linear.y=0
		msg.linear.z=0
		msg.angular.x=0
		msg.angular.y=0
		msg.angular.z=0
		pub.publish(msg)
		pub_l= rospy.Publisher('/mybot/leftWheel_effort_controller/command',Float64,queue_size=5)
		pub_r = rospy.Publisher('/mybot/rightWheel_effort_controller/command',Float64,queue_size=5)
		pub_l.publish(0.0)
		pub_r.publish(0.0)

def publisherr():
	
	
	rospy.init_node('publisher',anonymous=True)
	msg = Twist()
	pub_l = rospy.Publisher('/mybot/leftWheel_effort_controller/command',Float64,queue_size=5)
	pub_r = rospy.Publisher('/mybot/rightWheel_effort_controller/command',Float64,queue_size=5)
	pub   = rospy.Publisher('/mybot/cmd_vel',Twist,queue_size=5)
	
	with keyboard.Listener(on_press=on_press, on_release=on_release) as listner:
		listner.join()
	rospy.spin()
	

if __name__ == '__main__':
	publisherr()
