#!/usr/bin/env python

#import rospy
#import std_mesgs
import pyttsx

talker = pyttsx.init()
isAuthorized = false
isShannon = false
isHuman = false
isMoving = false
#The following if loop should be initiated after an intruder is detected
if isHuman:
	if isShannon or isAkash or isSam or isRollin:
		isAuthorized = true
	if isAuthorized:
		talker.say('Hello,Master! Welcome back.')
	if not isAuthorized:
		talker.say('You do not have clearance to enter this space. Your presence has been noted and reported. Leave')
if not isHuman:
	if isMoving:
		talker.say('Leave or be neutralized')
		#the robot should the attack
	if not isMoving:
		talker.say('New object detected!')
		#have robot report to Master

#while not rospy.is_shutdown():
#	rate.sleep()
		
