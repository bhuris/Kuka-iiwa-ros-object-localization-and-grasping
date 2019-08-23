#!/usr/bin/env python

# KUKA API for ROS

# Marhc 2016 Saeid Mokaram  saeid.mokaram@gmail.com
# Sheffield Robotics    http://www.sheffieldrobotics.ac.uk/
# The university of sheffield   http://www.sheffield.ac.uk/

# This script generats a ROS node for comunicating with KUKA iiwa
# Dependencies: conf.txt, ROS server, Rospy, KUKA iiwa java SDK, KUKA iiwa robot.

# This application is intended for floor mounted robots.
#######################################################################################################################
from client_lib import *
import time
# RECIEVE DATA
import socket 
# Making a connection object.
my_client = kuka_iiwa_ros_client()

# Wait until iiwa is connected zzz!
while (not my_client.isready): pass
print('Started!')

# Initializing Tool 1
my_client.send_command('setTool tool1')

# Initializing
my_client.send_command('setJointAcceleration 1.0')  # If the JointAcceleration is not set, the defult value is 1.0.
my_client.send_command('setJointVelocity 1.0')      # If the JointVelocity is not set, the defult value is 1.0.
my_client.send_command('setJointJerk 1.0')          # If the JointJerk is not set, the defult value is 1.0.
my_client.send_command('setCartVelocity 100')     # If the CartVelocity is not set, the defult value is 100   
time.sleep(15)    
s = socket.socket()         
print ("Socket successfully created")
port = 12345               
s.bind(('', port))        
print ("socket binded to %s" %(port))
 
# put the socket into listening mode
s.listen(5)     
print ("socket is listening" )          
c, addr = s.accept()     
print ('Got connection from', addr)
noofrecv = 0
print('after this data')
noofrecv = 0
allData = []
while noofrecv<3:
  data=c.recv(1024).decode()
  allData = allData + [x for x in data.split('\n') if x != '']
  print('dance dance\n')
  if data == 'bye' :break
  noofrecv +=1
for command in allData:
  my_client.send_command(command)
  print(command)
  raw_input("next")
c.close()




# Move to the exact start position.
#my_client.send_command('setPositionXYZABC 727.83 93.46 562.71 142.42 4.71 173.69 ptp')  # ptp motions move with setJointAcceleration

time.sleep(2)

#my_client.send_command('setPositionXYZABC 727.83 93.46 291.43 142.42 4.71 173.69 ptp')  # ptp motions move with setJointAcceleration


