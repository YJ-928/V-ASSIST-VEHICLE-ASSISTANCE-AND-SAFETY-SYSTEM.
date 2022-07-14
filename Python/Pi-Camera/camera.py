# import libraries
from picamera import PiCamera
import time

# Initialize object,
# it requires minimum 2 secands to initialize.
camera = PiCamera()
time.sleep(2)

# Code to Capture an image
# and save it in /home/pi/Pictures/img.jpg directory
camera.capture("/home/pi/Pictures/img.jpg")

# Capture image with custom options,
# Include timestamp to the file name
camera.resolution = (1280, 720)
camera.vflip = True
#camera.contrast = 10
#camera.image_effect = "negative"
time.sleep(2)
file_name = "/home/pi/Pictures/img_" + str(time.time()) + ".jpg"
camera.capture(file_name)


file_name = "/home/pi/Pictures/video_" + str(time.time()) + ".h264"
print("Recording Video...")
camera.start_recording(file_name)
camera.wait_recording(5)
camera.stop_recording()
print("Video Recording Saved.")
