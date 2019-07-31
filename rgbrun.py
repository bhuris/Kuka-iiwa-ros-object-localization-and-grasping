#@author: Carlos Torres <carlitos408@gmail.com>

import numpy as np
import cv2
from primesense import openni2#, nite2
from primesense import _openni2 as c_api

dist ='/home/ub2/Install/kinect/openni2/OpenNI2/Bin/x64-Release'



openni2.initialize(dist) #
if (openni2.is_initialized()):
    print ("openNI2 initialized")
else:
    print ("openNI2 not initialized")

dev = openni2.Device.open_any()
rgb_stream = dev.create_color_stream()

## Check and configure the depth_stream -- set automatically based on bus speed
print ('The rgb video mode is', rgb_stream.get_video_mode()) # Checks rgb video configuration
rgb_stream.set_video_mode(c_api.OniVideoMode(pixelFormat=c_api.OniPixelFormat.ONI_PIXEL_FORMAT_RGB888, resolutionX=1280, resolutionY=960, fps=30))

rgb_stream.start()

## Use 'help' to get more info
# help(dev.set_image_registration_mode)


def get_rgb():
    """
    Returns numpy 3L ndarray to represent the rgb image.
    """
    bgr   = np.fromstring(rgb_stream.read_frame().get_buffer_as_uint8(),dtype=np.uint8).reshape(960,1280,3)
    #bgr   = np.rot90(bgr,3)
    bgr   = np.flipud(bgr)
    rgb   = cv2.cvtColor(bgr,cv2.COLOR_BGR2RGB)
    return rgb    
#get_rgb
s=0
cv2.imwrite("ex2_"+str(s)+'.png', get_rgb())
## main loop

done = False
while not done:
    key = cv2.waitKey(1) & 255
    ## Read keystrokes
    if key == 27: # terminate
        print ("\tESC key detected!")
        done = True
    elif chr(key) =='s': #screen capture
        print ("\tSaving image {}".format(s))
        cv2.imwrite("ex2_"+str(s)+'.png', rgb)
        #s+=1 # uncomment for multiple captures
    	#cv2.VideoWriter('outpytemp.mp4',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (960,1280))    
    #RGB
    rgb = get_rgb()

    ## Display the stream syde-by-side
    cv2.imshow('rgb', rgb)
# end while

cv2.destroyAllWindows()
rgb_stream.stop()
openni2.unload()
print ("Terminated")
