"""All the required modules/functions available here."""
import RPi.GPIO as GPIO
from config import gpio

front_pwm = None
def robo_move(direction='forward'):
    '''Responsible for moving the robo.
       direction can be both forward and reverse
    '''
    return true

def _control_servo():
    '''Control the movement/ angle of servo.'''
    front_pwm.start(2.5)# starting duty cycle ( it set the servo to 0 degree )
    try:
        while True:
            for x in range(len(control)):
                p.ChangeDutyCycle(control[x])
                time.sleep(0.5)
                print x
        except KeyboardInterrupt:
            GPIO.cleanup()

def detect_obstacle_dist():
    '''Calculate the distance of obstacle.'''
    return True

def robo_stop():
    '''Stop the movement of robo.'''
    return True

def robo_init():
    '''Init the robo GPIO conf and get ready for action.'''
    GPIO.setmode(GPIO.BCM)
    # servo setup
    GPIO.setup(gpio['servo']['front_trigger'],GPIO.OUT) # front
    front_pwm = GPIO.PWM(gpio['servo']['front_trigger'], 50)
