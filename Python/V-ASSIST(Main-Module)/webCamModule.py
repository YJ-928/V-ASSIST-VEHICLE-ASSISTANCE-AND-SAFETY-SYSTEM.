# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640 , 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640 , 480))
# allow the camera to warmup
time.sleep(0.1)

def getImg():
    # capture frames from the camera
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        # grab the raw NumPy array representing the image, then initialize the timestamp
        # and occupied/unoccupied text
        image = frame.array
        #rawCapture.truncate(0)
        return image
    
if __name__ == '__main__':
    while True:
        img = getImg()
        cv2.imshow("Frame", img)