#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Float64
from geometry_msgs.msg import Twist

def callback(data):
	ranges=data.ranges
	'''if (ranges[0] != float('Inf')) & (ranges[1] != float('Inf')) & (ranges[2] != float('Inf')) & (ranges[3] != float('Inf')):
		goahead()
	if (ranges[3] != float('Inf')) & (ranges[4] != float('Inf')) & (ranges[5] != float('Inf')) & (ranges[6] != float('Inf')):
		goback()
	if ranges[0] != float('Inf'):
		print('right object detected')
		goleft()
	if ranges[3] != float('Inf'):
		goright()
		print('ahead object detected')
	if (ranges[3] == float('Inf')) & (ranges[4] == float('Inf')) & (ranges[5] == float('Inf')) & (ranges[6] == float('Inf')):
		print('rasta saaf hai bhiya')
		goahead()
		'''
	if (ranges[4] == float('Inf')) & (ranges[5] == float('Inf')):
		goahead()
	else:
		if (ranges[6] != float('Inf')) & (ranges[7] != float('Inf')):
			goright()
		elif (ranges[2] != float('Inf')) & (ranges[3] != float('Inf')):
			goleft()
		

def goahead():
	msg = Twist()
	pub = rospy.Publisher('/mybot/cmd_vel',Twist,queue_size=5)
	pub_l= rospy.Publisher('/mybot/leftWheel_effort_controller/command',Float64,queue_size=5)
	pub_r = rospy.Publisher('/mybot/rightWheel_effort_controller/command',Float64,queue_size=5)
	pub_l.publish(0.0)
	pub_r.publish(0.0)
	msg.linear.x=.5
	msg.linear.y=0
	msg.linear.z=0
	msg.angular.x=0
	msg.angular.y=0
	msg.angular.z=0
	#msg.speed=1
	pub.publish(msg)

def goback():
	msg = Twist()
	pub = rospy.Publisher('/mybot/cmd_vel',Twist,queue_size=5)
	pub_l= rospy.Publisher('/mybot/leftWheel_effort_controller/command',Float64,queue_size=5)
	pub_r = rospy.Publisher('/mybot/rightWheel_effort_controller/command',Float64,queue_size=5)
	pub_l.publish(0.0)
	pub_r.publish(0.0)
	msg.linear.x=-.5
	msg.linear.y=0
	msg.linear.z=0
	msg.angular.x=0
	msg.angular.y=0
	msg.angular.z=0
	#msg.speed=1
	pub.publish(msg)

def goright():
	msg = Twist()
	pub = rospy.Publisher('/mybot/cmd_vel',Twist,queue_size=5)
	pub_l= rospy.Publisher('/mybot/leftWheel_effort_controller/command',Float64,queue_size=5)
	pub_r = rospy.Publisher('/mybot/rightWheel_effort_controller/command',Float64,queue_size=5)
	pub_l.publish(10.0)
	pub_r.publish(-10.0)
	msg.linear.x=1
	msg.linear.y=0
	msg.linear.z=0
	msg.angular.x=0
	msg.angular.y=0
	msg.angular.z=0
	#msg.speed=1
	pub.publish(msg)

def goleft():
	msg = Twist()
	pub = rospy.Publisher('/mybot/cmd_vel',Twist,queue_size=5)
	pub_l= rospy.Publisher('/mybot/leftWheel_effort_controller/command',Float64,queue_size=5)
	pub_r = rospy.Publisher('/mybot/rightWheel_effort_controller/command',Float64,queue_size=5)
	pub_l.publish(-10.0)
	pub_r.publish(10.0)
	msg.linear.x=1
	msg.linear.y=0
	msg.linear.z=0
	msg.angular.x=0
	msg.angular.y=0
	msg.angular.z=0
	#msg.speed=1
	pub.publish(msg)

def listener():
	rospy.init_node('listener', anonymous=True)
	rospy.Subscriber('/mybot/laser/scan', LaserScan, callback)
	
	rospy.spin()

if __name__ == '__main__':
	listener()
