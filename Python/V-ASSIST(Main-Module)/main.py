from motorModule import Motor
 
motor= Motor(13,27,17,10,9,12)
 
def main():
    print("Moving Forward")
    motor.move(0.6,0.2,5)
    motor.stop(2)
    print("Moving Backward")
    motor.move(-0.6,0,5)
    motor.stop(2)
    '''print("Moving Left")
    motor.move(0.6,0.3,2)
    motor.stop(2)
    print("Moving Right")
    motor.move(0.6,-0.3,2)
    motor.stop(2)'''
 
if __name__ == '__main__':
    while True:
        main()