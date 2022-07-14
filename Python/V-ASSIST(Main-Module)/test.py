#!/usr/bin/env python
# -*- coding: utf-8 -*-
# lsusb to check device name
#dmesg | grep "tty" to find port name

import serial
import time
from keyboardModule import Keyboard 




if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.reset_input_buffer()
    keyboard = Keyboard()
    keyboard.init()
    msg = b""
    while True:
        
        
        if keyboard.getKey('DOWN'):
            msg = bytes("mov(0, 0)",'utf-8')
        elif keyboard.getKey('LEFT'):
            msg = bytes("mov(0.4, 0.5)",'utf-8')
        elif keyboard.getKey('RIGHT'):
            msg = bytes("mov(0.4, -0.5)",'utf-8')
        else:
            msg = bytes("mov(0.4, 0)",'utf-8')
        # send the DATA to ARDUINO
        
        #msg = bytes("mov(" + str(0.4) + ", " + str(-curveVal*sen) + ")\n",'utf-8')
        ser.write(msg)
        line = ser.readline().decode('utf-8').rstrip()
        #print(line)
        

