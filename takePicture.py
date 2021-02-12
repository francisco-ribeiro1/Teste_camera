from gpiozero import Button
from picamera import PiCamera
from datetime import datetime
from signal import pause
from time import sleep

clickButton = Button (6)

#camera = PiCamera()
#camera = PiCamera(resolution=(3280, 2464))
camera = PiCamera()
print(camera.MAX_RESOLUTION)

def capture():
    timestamp = datetime.now().isoformat()
    camera.capture('/home/pi/Pictures/%s.png' % timestamp)

clickButton.when_pressed = capture

#sleep(3)
#capture()
#sleep(10)

pause()