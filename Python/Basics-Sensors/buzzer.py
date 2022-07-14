# Start by importing Buzzer from the gpiozero module and pause from the signal module:
from gpiozero import Buzzer
from signal import pause

# Next, create an instance of Buzzer called buzzer
# Set the GPIO pin to 4:
buzzer = Buzzer(17)

# Call the .beep() method on buzzer. 
# Set the on_time and off_time parameters to 0.5. 
# This will make the buzzer beep every half second:
buzzer.beep(0.5, 0.5)

pause()
