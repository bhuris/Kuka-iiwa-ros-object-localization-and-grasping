# Kuka-iiwa-ros-object-localization-and-grasping 
By Bhubodinn Wongsa-ngasri / Bhuris Sridurongrit

The reinforcement learning module is developing.
This project is using KUKA iiwa 7 R800 and Robotiq Gripper 3 Fingers 
Openni2 camera (using primesense)
Setup on ubuntu 16.04

Ros kinetic dep

[Watch the video](https://youtu.be/wn06D7Y_zG4).
## Credits

A Keras implementation of YOLOv3 (Tensorflow backend) inspired by [allanzelener/YAD2K](https://github.com/allanzelener/YAD2K).

Ros interface for kuka iiwa from  [jonaitken/KUKA-IIWA-API](https://github.com/jonaitken/KUKA-IIWA-API).

Openni2 camera binding to python is from [elmonkey/Python_OpenNI2](https://github.com/elmonkey/Python_OpenNI2).

Ros iiwa stack support and api from [IFL-camp/iiwa_stack](https://github.com/IFL-CAMP/iiwa_stack).


---

## Project Phase (time usage)
1.Setup and Install KUKA hardware
(https://www.kuka.com/-/media/kuka-downloads/imported/48ec812b1b2947898ac2598aff70abc0/spez_lbr_iiwa_en.pdf?rev=9f39c2bdbc9f415e819fea3a7b0a4d16?modified=1075304703)

2.Install ROS Kinetic

3.Setup Ros interface (1Week)Setup&Installation 3D/Depth Camera hardware

4.Setup Coding Environment

5.Study Deep Learning (by P’Boss and P’Pao)

6.Pick and Place (basic robot operation via ROS)

7.Object recognition and localization 

8.Reinforcement pick and place

9.Summary



---
### Setup and Install KUKA 
	Firstly might follow this procedure to configure robot controller
PTT DITC’s Kuka Hardware
-	KUKA LBR iiwa 7 R800
https://www.kuka.com/en-de/products/robot-systems/industrial-robots/lbr-iiwa
-	3-Finger Adaptive Robot Gripper
https://robotiq.com/products/3-finger-adaptive-robot-gripper 

Install and check hardware (manipulator and control cabinet)
Connect ethernet cable to port X66 of control cabinet ,the other side are connected to computer
Calibrate TCP of tool (3finger gripper)
The repo of iiwa_stack require ROS kinetic or melodic only
Setup sunrise cabinet preference
Get in touch with gripper interface (via Remote I/O extension card)
Wiring network are shown below
Contact sales representative “ROSSmartServo” Extension Software 
Test motion by using jog pad in smartpad

### Install ROS 
(http://wiki.ros.org/kinetic/Installation/Ubuntu)
ROS Kinetic ONLY supports Wily (Ubuntu 15.10), Xenial (Ubuntu 16.04) and Jessie (Debian 8) for debian packages.

### Setup Ros interface
(https://github.com/IFL-CAMP/iiwa_stack)
Connect an ethernet cable between the X66 port of your SUNRISE Cabinet and your ROSmachine
By default the SUNRISE Cabinet IP address is 172.31.1.147. Setup the network interface on the ROS machine to be in the same subnet. (e.g. 172.31.1.150). Ping the SUNRISE Cabinet from your ROS machine to check that everything is fine.
Clone, build and setup iiwa_stack on your ROS machine.
Clone and setup a Sunrise Project with iiwa_stack on your SUNRISE Cabinet.
Follow wiki on iiwa_stack repo
Using IIWA -API Matlab toolbox for servo control extension from github
The position from camera raw (pixel on screen) is fetch to camera calibration function that 
Setup Coding Environment (1 Week+)
Install Python 3.5.2 and update python 2.7 for ROS kinetic
Check package of Ros install properly

Pick and Place (basic robot operation via ROS) 2Weeks
Implement by using YOLO-v3 model and pretrained weight by Darknet 

Object recognition and localization 1Week
Reinforcement pick and place 1Month
Summary
Finish milestone 1



### Setup Coding Environment
install cuda toolkit and cudnn 
install graphic card driver (Nvidia)
download yolo model
download pretrain weight from darknet
wget https://pjreddie.com/media/files/yolov3.weights
python convert.py yolov3.cfg yolov3.weights model_data/yolo.h5
python yolo_video.py [OPTIONS...] --image, for image detection mode, OR
python yolo_video.py [video_path] [output_path (optional)]

default ip of iiwa cabinet is 172.31.1.147
```

For Tiny YOLOv3, just do in a similar way, just specify model path and anchor path with `--model model_file` and `--anchors anchor_file`.

usage: yolo_video.py [-h] [--model MODEL] [--anchors ANCHORS]
                     [--classes CLASSES] [--gpu_num GPU_NUM] [--image]
                     [--input] [--output]
```
you need to config calibration function on that repo to config perspective effect due to camera angle is not bird eye view.

### Pick and Place (basic robot operation via ROS)
runpg.py is set to send socket packet via TCP to another computer to command robot
the command is list in [command](https://github.com/jonaitken/KUKA-IIWA-API/blob/master/Instruction.pdf)
set the standby and reach height from this file
the code is set to pick up only cup you can edit and change it to wherever you want (and darknet model can be detect !!)
### Object recognition and localization 
using bounding box and complex logarithm regression process to calculate the variable to fix position
for more information 
Object localization in images using simple CNNs and Keras [lars76/object-localization](https://github.com/lars76/object-localization).
### Reinforcement pick and place
///currently work in process
### Summary
to run program you need to open your workspace path
my worked procedure is following this sequence

1.on Ros machine run 'roscore'

2.if the command is working then run 'server launch file' 'server_V30032017.py'

3.on cabinet smartpad run iiwa api java file
make sure that openni is already config and camera is in (using lsusb)

4.run runrgblowres.py to check camera

5.run yolo_video.py to check tensorflow backend (load model and pretrain weight completed)

6.the main program is runpg.py 
when the camera on screen prompt is appear you adjust the position reach
when the image is loaded and 'tensorflow backend' appear

7.run posi.py on rosmachine

8.when inferencing process is done robot will move to stanby and reach the object that is already set

the default is 'cup'
The test environment is
    - Python 3.5.2
    - Keras 2.1.5
    - tensorflow 1.6.0


