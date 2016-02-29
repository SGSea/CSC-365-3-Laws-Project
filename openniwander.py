#!/usr/bin/env python

import random
import rospy
from sensor_msgs.msg import PointCloud2
import math

# Every Python Controller needs these lines
import roslib; roslib.load_manifest('project1')

# The velocity command message
from geometry_msgs.msg import Twist


def callback(data):
    distance = .7
    angleTurn = random.random()
    # If a point in the range is less than a distance determined in the cmd line input, stop moving forward and turn until you can resume forward motion - at which point stop turning.
   
    no_nans = [n for n in data.fields if not math.isnan(n)]
    if min(no_nans) < distance:
        command.linear.x = 0
        #if angleTurn >= .2:
        #   command.angular.z = .5
        #else:
        #command.angular.z = -.5
    else:
        command.linear.x = 0.5
        #command.angular.z = 0
   

# Main function
if __name__ == '__main__':
   
    rospy.init_node('move')

    # A publisher for the move data
    pub = rospy.Publisher('mobile_base/commands/velocity', Twist, queue_size=10)
    rospy.Subscriber('scan', PointCloud2, callback)

    # Drive forward at a given speed.  The robot points up the x-axis.
    command = Twist()
    command.linear.x = .3
    command.linear.y = 0.0
    command.linear.z = 0.0
    command.angular.x = 0.0
    command.angular.y = 0.0
    command.angular.z = 0.0

    # Loop at 10Hz, publishing movement commands until we shut down.
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        pub.publish(command)
        rate.sleep()

