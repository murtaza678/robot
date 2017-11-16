#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32
from sensor_msgs.msg import LaserScan


def callback(data):
	ranges=data.ranges
	if ranges[3] != float('Inf'):
		print('right object detected')
	if ranges[4] != float('Inf'):
		print('ahead object detected')
	if ranges[5] != float('Inf'):
		print('ahead object detected')
	if ranges[6] != float('Inf'):
		print('left object detected')
	if (ranges[3] == float('Inf')) & (ranges[4] == float('Inf')) & (ranges[5] == float('Inf')) & (ranges[6] == float('Inf')):
		print('rasta saaf hai bhiya')
		



def listener():
	rospy.init_node('listener', anonymous=True)
	rospy.Subscriber('/mybot/laser/scan', LaserScan, callback)
	rospy.spin()

if __name__ == '__main__':
	listener()
