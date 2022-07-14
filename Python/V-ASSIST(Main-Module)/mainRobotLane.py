#!/usr/bin/env python
# -*- coding: utf-8 -*-
# lsusb to check device name
#dmesg | grep "tty" to find port name

from laneDetectionModule import getLaneCurve
#import webCamModule
import serial
import time
from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
from keyboardModule import Keyboard 

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (480, 240)
camera.vflip = True
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(480, 240))


# allow the camera to warmup
time.sleep(0.1)

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.reset_input_buffer()
    keyboard = Keyboard()
    keyboard.init()
    msg = b""
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        # grab the raw NumPy array representing the image, then initialize the timestamp
        # and occupied/unoccupied text
        img = frame.array
        """curveVal= getLaneCurve(img,1)

        sen = 1.3  # SENSITIVITY
        maxVAl= 0.3 # MAX SPEED
        if curveVal>maxVAl:curveVal = maxVAl
        if curveVal<-maxVAl: curveVal =-maxVAl
        #print(curveVal)
        if curveVal>0:
            sen =1.7
            if curveVal<0.05: curveVal=0
        else:
            if curveVal>-0.08: curveVal=0
        
        """
        if keyboard.getKey('DOWN'):
            msg = bytes("mov(0, 0)",'utf-8')
        if keyboard.getKey('LEFT'):
            msg = bytes("mov(0.4, 0.5)",'utf-8')
        if keyboard.getKey('RIGHT'):
            msg = bytes("mov(0.4, -0.5)",'utf-8')
        # send the DATA to ARDUINO
        
        #msg = bytes("mov(" + str(0.4) + ", " + str(-curveVal*sen) + ")\n",'utf-8')
        ser.write(msg)
        msg = bytes("mov(0.4, 0)",'utf-8')
        line = ser.readline().decode('utf-8').rstrip()
        print(line)
        
        key = cv2.waitKey(1) & 0xFF
        # clear the stream in preparation for the next frame
        rawCapture.truncate(0)
        # if the `q` key was pressed, break from the loop
        if key == ord("q"):
            break
