"""All the required modules/functions available here."""
import time
import RPi.GPIO as GPIO
from config import gpio, threshold

def __robo_wheel_control(wheel, direction='forward', mode='HIGH'):
    '''Move wheels forward/reverse.'''
    if direction == 'forward':
        GPIO.output(gpio['wheel'][wheel + '_forward'], eval('GPIO.'+ mode))
    if direction == 'reverse':
        GPIO.output(gpio['wheel'][wheel + '_reverse'], eval('GPIO.'+ mode))

def __robo_right_wheel(direction='forward'):
    '''Move left wheel forward.'''
    return True

def robo_move(direction='forward'):
    '''Responsible for moving the robo.
       direction can be both forward and reverse
    '''
    return true

def detect_obstacle_dist():
    '''Calculate the distance of obstacle.'''
    front_pwm = GPIO.PWM(gpio['servo']['front_trigger'], 50)
    front_pwm.start(2.5) # set servo to 0 degree.
    control = threshold['servo_cycle']
    try:
        while True:
            for x in range(len(control)):
                front_pwm.ChangeDutyCycle(control[x])
                time.sleep(0.5)
                print(__get_distance())
    except KeyboardInterrupt:
        GPIO.cleanup()

def __get_distance():
    '''Get distance between robo and object.'''
    # set Trigger to HIGH
    GPIO.output(gpio['ultrasensor']['front_trigger'], True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(gpio['ultrasensor']['front_trigger'], False)
 
    StartTime = time.time()
    StopTime = time.time()

    # save StartTime
    while GPIO.input(gpio['ultrasensor']['front_echo']) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(gpio['ultrasensor']['front_echo']) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
    return distance    

def robo_stop():
    '''Stop the movement of robo.'''
    return True

def robo_init():
    '''Init the robo GPIO conf and get ready for action.'''
    GPIO.setmode(GPIO.BCM)

    # servo setup
    GPIO.setup(gpio['servo']['front_trigger'],GPIO.OUT) # front

    # setup Ultrasonic Sensors
    GPIO.setup(gpio['ultrasensor']['front_trigger'], GPIO.OUT)
    GPIO.setup(gpio['ultrasensor']['front_echo'], GPIO.IN)
    
