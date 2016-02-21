#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import std_msgs
import pyttsx

talker = pyttsx.init()
isAuthorized = False
isShannon = False
isAkash = False
isSam = False
isRollin = False
isHuman = False
isMoving = False
react = "reacting"
#The following if loop should be initiated after an intruder is detected
if isHuman:
	if isShannon or isAkash or isSam or isRollin:
		isAuthorized = true
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
print react
talker.say(react)
talker.runAndWait()

rospy.init_node('reaction_publisher')
pub = rospy.Publisher('reactions', String, queue_size=30)
rate = rospy.Rate(2)

while not rospy.is_shutdown():
	rospy.loginfo(react)
	pub.publish(react)
	rate.sleep()

#def loop(self)
#	self.talker.startLoop(False)
#	while not rospy.is_shutdown():
#		self.talker.iterate()
#		time.sleep(0.1)
#	self.talker.endLoop()

