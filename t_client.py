#! /usr/bin/env python
# -*- coding=utf-8 -*-
import socket
import struct
import rospy
import time
from std_msgs.msg import Int32
from std_msgs.msg import String


#message proto
# id |  length | data
def send_msg(sock, msg):
    # Prefix each message with a 4-byte id and length (network byte order)
    sock.sendall(msg)


def odomCallback(msg):
    global odom_socket
    print(msg)
    data='google'
    send_msg(odom_socket,data)

odom_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
odom_socket.connect(('127.0.0.1',8002))
rospy.init_node('server_node')

#rospy.Subscriber('/switch',PoseWithCovarianceStamped,odomCallback)
#rospy.Subscriber('/switch',std_msgs/Int32,odomCallback)
rospy.Subscriber('/switch',String,odomCallback)

rospy.spin()
