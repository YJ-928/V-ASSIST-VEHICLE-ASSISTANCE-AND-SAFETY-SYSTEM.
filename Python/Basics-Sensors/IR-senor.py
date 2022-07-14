import RPi.GPIO as IO

import time

IO.setwarnings(False)

IO.setmode(IO.BCM)


IO.setup(2,IO.OUT) #GPIO 2 -> Red LED as output

IO.setup(3,IO.OUT) #GPIO 3 -> Green LED as output

IO.setup(18,IO.IN) #GPIO 18 -> IR sensor as input


while 1:


    if(IO.input(18)==True): #object is far away

        IO.output(2,True) #Red led ON

        IO.output(3,False) # Green led OFF
        
        print("Obstacle Not Detected")
    

    if(IO.input(18)==False): #object is near

        IO.output(3,True) #Green led ON

        IO.output(2,False) # Red led OFF
        
        print("Obstacle Detected")
        print(".......................................................")
