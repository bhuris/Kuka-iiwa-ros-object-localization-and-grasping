import os
import subprocess
import time
from Calibration_Function import *
import socket     
import time 
pathopening = 'cd ~/Desktop/pttintern-kuka1' #in ubuntu
os.system(pathopening)
time.sleep(1)
snap = 'python3 rgbrunlowres.py'
os.system(snap)

def callyolo():
	yolopath_str = 'python3 yolo_video.py --image --gpu_num 0'
	outfromyo1 = os.popen(yolopath_str).read()
	#print(outfromyo1)
	dataraw=outfromyo1.split('@')
	#print(dataraw)
	return dataraw

extract = callyolo()
data1=extract[2]
data2=extract[4]
data1.replace("\n", "")
data2.replace("\n", "")    
line1=data1.split()
line2=data2.split()
posix_1=line1[5]
posiy_1=line1[8]
posix_2=line2[5]
posiy_2=line2[8]
obj1x,obj1y=Calibration(eval(posix_1),eval(posiy_1))
obj2x,obj2y=Calibration(eval(posix_2),eval(posiy_2))
print('obj1-2d',obj1x,obj1y)
print('obj2-2d',obj2x,obj2y)
print(obj1x,obj1y,obj2x,obj2y)
s = socket.socket()        
port = 12345               
s.connect(('172.31.1.50', port))
sup ='ok'
normal_abc = ' 131.09 3.22 177.29'
mot_mode = ' ptp\n'
z_above = ' 562.71'
z_reach = ' 291.00'
com1 = 'setPositionXYZABC '+str(obj1x)+' '+str(obj1y)+z_above+normal_abc+mot_mode
com2 = 'setPositionXYZABC '+str(obj1x)+' '+str(obj1y)+z_reach+normal_abc+mot_mode
com3 = 'setPositionXYZABC '+str(obj1x)+' '+str(obj1y)+z_above+normal_abc+mot_mode
com4 = 'setPositionXYZABC '+str(obj2x)+' '+str(obj2y)+z_above+normal_abc+mot_mode
com5 = 'setPositionXYZABC '+str(obj2x)+' '+str(obj2y)+z_reach+normal_abc+mot_mode
com6 = 'setPositionXYZABC '+str(obj2x)+' '+str(obj2y)+z_above+normal_abc+mot_mode
stby = 'setPositionXYZABC '+'411.05'+' -59.80'+' 520'+normal_abc+mot_mode

#com3 = obj2x,' ',obj2y,' '

def sendcomgoto(datast):
    input_string = datast.encode()
    s.sendall(input_string)
sendcomgoto(sup)
sendcomgoto(com1)
sendcomgoto(com2)
sendcomgoto(com3)
sendcomgoto(stby)
sendcomgoto(com4)
sendcomgoto(com5)
sendcomgoto(com6)
sendcomgoto(stby)
s.close()



