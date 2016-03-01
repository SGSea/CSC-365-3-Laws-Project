#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import std_msgs
import pyttsx
import unittest

talker = pyttsx.init()

#the following parameters are now initialized in patrol.launch
#use rosparam set PARAM VALUE to get different results for now

#rospy.set_param('notice', False)
#rospy.set_param('isShannon',  False)
#rospy.set_param('isAkash',  False)
#rospy.set_param('isSam', False)
#rospy.set_param('isRollin', False)
#rospy.set_param('isHuman',  False)
#rospy.set_param('isMoving', False)
isAuthorized = False
react = "reacting"
oldReaction = react
statement = "Initialized"

#The following if loop should be initiated after an intruder is detected
if rospy.get_param('notice'):
	if rospy.get_param('isHuman'):
		if rospy.get_param('isShannon') or rospy.get_param('isAkash') or rospy.get_param('isSam') or rospy.get_param('isRollin'):
			isAuthorized = True
		if isAuthorized:
			react = "Hello, Master! Welcome back."
		if not isAuthorized:
			react = "You do not have clearance to be here. Leave"
	if not rospy.get_param('isHuman'):
		if rospy.get_param('isMoving'):
			react = "Leave or be neutralized"
			#the robot should then attack, with Sam's code
		if not rospy.get_param('isMoving'):
			react = "A new object has been detected"
			#have robot report to Master--publisher
	if react != oldReaction:
		oldReaction = react
		if isAuthorized:
			statement = "I am resuming my duties"
		if not isAuthorized:
			statement = "I am now investigating this occurrence"

		talker.say(react)
		talker.runAndWait()
	rospy.set_param('notice', False)

#creates a publisher with updates on the node's status
rospy.init_node('reaction_publisher')
pubReactions = rospy.Publisher('reactions', String, queue_size=1)
rate = rospy.Rate(1)

while not rospy.is_shutdown():
	rospy.loginfo(react + "..." + statement)
	pubReactions.publish(react + "..." + statement)
	rate.sleep()
