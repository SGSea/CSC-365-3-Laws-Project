#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import std_msgs
import pyttsx

talker = pyttsx.init()
notice = True
isAuthorized = False
isShannon = False
isAkash = False
isSam = False
isRollin = False
isHuman = False
isMoving = True
react = "reacting"
oldReaction = react
#The following if loop should be initiated after an intruder is detected
if notice:
	if isHuman:
		if isShannon or isAkash or isSam or isRollin:
			isAuthorized = True
		if isAuthorized:
			react = "Hello, Master! Welcome back."
		if not isAuthorized:
			react = "You do not have clearance to be here. Leave"
	if not isHuman:
		if isMoving:
			react = "Leave or be neutralized"
			#the robot should the attack
		if not isMoving:
			react = "A new object has been detected"
			#have robot report to Master
	if react != oldReaction:
		statement = react
		print statement
		oldReaction = react
		if isAuthorized:
			statement = "I am resuming my duties"
		if not isAuthorized:
			statement = "I am now investigating this occurrence"

		talker.say(react)
		talker.runAndWait()

rospy.init_node('reaction_publisher')
pubReactions = rospy.Publisher('reactions', String, queue_size=30)
rate = rospy.Rate(2)

while not rospy.is_shutdown():
	rospy.loginfo(statement)
	pubReactions.publish(statement)
	oldReaction = react
	rate.sleep()

   # A subscriber for the camera
def callback(data):
	rospy.loginfo("I heard ", data.data)
	print data.data
def listener():
	rospy.init_node('detect_listener')
	sub = rospy.Subscriber('testPub', String, callback)
	message = data.string
	rospy.spin()
