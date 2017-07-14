#! /usr/bin/env python
# -*- coding=utf-8 -*-
import socket
import time,os,fcntl
import struct
import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped,PoseStamped
from std_msgs.msg import String
#message proto
# id | length | data
def recv_msg(sock):
    ret = ''
    try:
        # Read message length and unpack it into an integer
		return recvall(sock, 1)
    except Exception ,e:
        return None



def recvall(sock, n):
    # Helper function to recv n bytes or return None if EOF is hit
    data = ''
    while len(data) < n:
        packet = sock.recv(1)
        if not packet:
            return None
        data += packet
    return data




#初始化socket，监听8000端口
odom_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
odom_socket.bind(('',8002))
odom_socket.listen(10)

(client,address) = odom_socket.accept()

rospy.init_node("client_node")
odom_pub = rospy.Publisher("/switch",String,queue_size=30)
r = rospy.Rate(10)

#设置noblock，否则会阻塞在接听，下面while不会一直循环，只有在有数据才进行下一次循环
fcntl.fcntl(client, fcntl.F_SETFL, os.O_NONBLOCK)

str_cc="googo"
while not rospy.is_shutdown():
    data = recv_msg(client)
    #if data:
    odom_pub.publish(str_cc)
    r.sleep()
    print(data)
