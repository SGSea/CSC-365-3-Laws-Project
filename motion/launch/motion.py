#!/usr/bin/python


# Every python controller needs these lines
import roslib; roslib.load_manifest('motion')
import rospy
import math
import cv2

# The velocity command message
from sensor_msgs.msg import LaserScan
from sensor_msgs.msg import Image


maximum_range = 4.5
#do we have a previous scan or is this the first scan
initialized = False
#keep track of scan index
count = 0
#previous scan
lastScan = []
#most recent scan
thisScan = []
#differences between scan ranges
changeMap = []
#average change in position
runningAvg = 0.0
pub = rospy.Publisher('motion_lines', LaserScan, queue_size=10)


#finds the index of the edge of the largest motion blob
def calculateBox():

    global runningAvg
    global changeMap
    global count
    leftEdgeIndex = 0
    rightEdgeIndex = 0
    consecutiveHits = 0
    maxHits = 0
    count = 0
    for i in changeMap:

        #change multiplier in if statement to adjust the sensitivity of motion detection
        if i > (2 * runningAvg):
            consecutiveHits = consecutiveHits + 1
            if consecutiveHits > maxHits:
                maxHits = consecutiveHits
                leftEdgeIndex = count - maxHits

        else:
            #if this is the largest blob yet, save where it ends
            if consecutiveHits == maxHits:
                rightEdgeIndex = count

            consecutiveHits = 0

        count = count + 1




def compareData():

    global lastScan
    global thisScan
    global count
    global runningAvg
    avgerSum

        count = 0
        for r in thisScan:

            #set nans to max_range instead and make change value negligable
            if math.isnan(r):
                    lastScan[count] = 4.5
                    changeMap[count] = -1.0
            
            else: #compute absolute change and save to changeMap

                if r < lastScan[count]:
                    changeMap[count] = lastScan[count]-r
                    
                else:
                    changeMap[count] = r-lastScan[count]
                
                #after comparison, overwrite lastScan to current value
                lastScan[count] = r
                #all non-nan values are included to find the average change
                avgerSum = avgerSum + changeMap[count]

        
            count = count + 1            
        #compute avg after for loop
        runningAvg = (runningAvg + (avgerSum/(count+1)))/2
        #publish data to find_object 
        sendData()


        

def callback(data): #scrape messege for range data
    
    global thisScan
    global lastScan
    global count
    global maximum_range

    #make sure we have something in lastScan
    if not initialized:
        count = 0
        maximum_range = data.max_range

        for r in data.ranges:

            #don't save nans set to max_range instead
            if math.isnan(r):
                lastScan[count] = maximum_range
            
            else: #save range value
                lastScan[count] = r

        initialized = True

    else: #save data to thisScan and compare to last scan
        thisScan = data.ranges
        compareData()
	
    pub.publish(changeMap)	





if __name__ == '__main__':
    rospy.init_node('motion')

    # A subscriber for the movement data
    sub = rospy.Subscriber( "scan", LaserScan, callback)
	
    
