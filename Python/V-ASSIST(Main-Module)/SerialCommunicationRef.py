#!/usr/bin/env python
# -*- coding: utf-8 -*-
# lsusb to check device name
#dmesg | grep "tty" to find port name

import serial,time


if __name__ == '__main__':
    print('Running. Press CTRL-C to exit.')
    with serial.Serial("/dev/ttyACM0", 9600, timeout=1) as arduino:
        time.sleep(0.1) #wait for serial to open
        if arduino.isOpen():
            print("{} connected!".format(arduino.port))
            try:
                while True:
                    cmd=input("Enter command (data,led0 or led1): ")
                    arduino.write(cmd.encode())
                    #time.sleep(0.1) #wait for arduino to answer
                    
                    while arduino.inWaiting()==0: pass
                    if  arduino.inWaiting()>0: 
                        answer=str(arduino.readline())
                        print("---> {}".format(answer))
                        if cmd=="data":
                            dataList=answer.split("x")
                            print("led state : {}".format(dataList[0]))
                            print("Analog input A0 : {}".format(dataList[1]))
                            print("Analog input A1: {}".format(dataList[2]))
                            
                            arduino.flushInput() #remove data after reading
                            
            except KeyboardInterrupt:
                print("KeyboardInterrupt has been caught.")
