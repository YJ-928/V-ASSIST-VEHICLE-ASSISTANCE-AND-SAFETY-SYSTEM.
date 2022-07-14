import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

IN1 = 27
IN2 = 17
IN3 = 10
IN4 = 9
ENA = 13
ENB = 12

GPIO.setup(IN1,GPIO.OUT)
GPIO.setup(IN2,GPIO.OUT)
GPIO.setup(IN3,GPIO.OUT)
GPIO.setup(IN4,GPIO.OUT)
GPIO.setup(ENA,GPIO.OUT)
GPIO.setup(ENB,GPIO.OUT)

PWMA = GPIO.PWM(ENA,100)
PWMA.start(0)
PWMB = GPIO.PWM(ENB,100)
PWMB.start(0)

while True:
    '''GPIO.output(IN1,GPIO.HIGH)
    sleep(1)
    GPIO.output(IN1,GPIO.LOW)
    sleep(1)
    GPIO.output(IN2,GPIO.HIGH)
    sleep(1)
    GPIO.output(IN2,GPIO.LOW)
    sleep(1)
    GPIO.output(IN3,GPIO.HIGH)
    sleep(1)
    GPIO.output(IN3,GPIO.LOW)
    sleep(1)
    GPIO.output(IN4,GPIO.HIGH)
    sleep(1)
    GPIO.output(IN4,GPIO.LOW)
    sleep(1)'''
    for duty in range(0,101,1):
        PWMA.ChangeDutyCycle(duty)
        sleep(0.01)
        PWMB.ChangeDutyCycle(duty)
        sleep(0.01)
    sleep(2)
    for duty in range(100,-1,-1):
        PWMA.ChangeDutyCycle(duty)
        sleep(0.01)
        PWMB.ChangeDutyCycle(duty)
        sleep(0.01)
    sleep(1)
# 22 FAULTY