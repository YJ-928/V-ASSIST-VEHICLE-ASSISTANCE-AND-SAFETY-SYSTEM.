from gpiozero import LED
from signal import pause

# create an instanc of LED called led
led = LED(4)
led.blink()

pause()
