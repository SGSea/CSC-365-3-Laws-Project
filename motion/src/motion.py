#!/usr/bin/python


# Every python controller needs these lines
import roslib; roslib.load_manifest('motion')
import rospy
import math

# The velocity command message
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

stopper = .7
initialized = False
count = 0
command = Twist()
lastScan = LaserScan()
changeMap = LaserScan()
avgerSum = 0.0

def callback(data):
    
    global initialized
    global count
    global lastScan
    global changeMap
    global command

    count = 0
    closest = float("inf")
    if initialized:
        
        for r in data.ranges:
            print "in for loop"
        
		
            if (not math.isnan(r)) and r < closest:
                closest = r

            if math.isnan(r):
                    lastScan.ranges[count] = 4.51
                    changeMap.ranges[count] = -1.0
                
            
            else:
                    changeMap.ranges[count] = math.abs(lastScan[count]-r)
                    lastScan.ranges[count] = r
                    avgerSum += changeMap.ranges[count]

        count = count + 1   
        sendData()         
        if closest < stopper:
            command.linear.x = 0
        
        
    else:
        lastScan = data
        initialized = True



		

if __name__ == '__main__':
    rospy.init_node('motion')

    # A publisher for the move data
    vidPub = rospy.Publisher('movement', LaserScan, queue_size=10)
    pub = rospy.Publisher('cmd_vel_mux/input/teleop', Twist, queue_size=10)
    sub = rospy.Subscriber( "scan", LaserScan, callback)
    


    #command = Twist()
    print 'freedom!'
    command.linear.x = 0.1
    command.linear.y = 0.0
    command.linear.z = 0.0
    command.angular.x = 0.0
    command.angular.y = 0.0
    command.angular.z = 0.0



    
# Loop at 10Hz, publishing movement commands until we shut down.
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
	#print "looping"
        pub.publish(command)
        rate.sleep()
	

def sendData():
    vidPub.publish(changeMap)
