#!/usr/bin/env python

#import rospy
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
#The following if loop should be initiated after an intruder is detected
if isHuman:
	if isShannon or isAkash or isSam or isRollin:
		isAuthorized = true
	if isAuthorized:
		talker.say('Hello,Master! Welcome back.')
		print "Welcomed Master"
	if not isAuthorized:
		talker.say('You do not have clearance to enter this space. Your presence has been noted and reported. Leave')
		print "Warned human intruder"
if not isHuman:
	if isMoving:
		talker.say('Leave or be neutralized')
		print "Warned intruder"
		#the robot should the attack
	if not isMoving:
		talker.say('New object detected!')
		print "Identified object"
		#have robot report to Master
talker.runAndWait()

#while not rospy.is_shutdown():
#	rate.sleep()
		
