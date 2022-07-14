# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.vflip = True
#camera.image_effect = "negative"
camera.resolution = (720, 480)


rawCapture = PiRGBArray(camera)

# allow the camera to warmup
time.sleep(0.1)

# grab an image from the camera
camera.capture(rawCapture, format="bgr")
image = rawCapture.array


# display the image on screen and wait for a keypress
cv2.imshow("Image", image)
cv2.waitKey(0) # Wait until user closesthe window
cv2.destroyAllWindows()
