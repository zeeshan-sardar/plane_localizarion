#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import NavSatFix
from datetime import datetime
import csv

def callback(data, writer):
    row = [data.header.stamp, data.latitude, data.longitude, data.altitude]
    rospy.loginfo( row)
    writer.writerow(row)
    
def listener(writer):

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('gps_log', anonymous=True)

    rospy.Subscriber("/fix", NavSatFix, callback, writer)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':

    now = datetime.now()
    dt_string = now.strftime("%d-%m-%Y %H:%M:%S")
    csv_file = 'gps_'+dt_string + ".csv"
    csvfile = open(csv_file, 'wb')    
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(['timestamp', 'latitude', 'longitude', 'altitude'])

    listener(writer)