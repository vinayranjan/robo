"""All the required modules/functions available here."""
import time
import RPi.GPIO as GPIO
from config import gpio, threshold


def __robo_wheel_control(wheel, direction='forward', mode='HIGH'):
    '''Move wheels forward/reverse.'''
    if direction == 'forward':
        time.sleep(0.01)
        GPIO.output(gpio['wheel'][wheel + '_forward'], eval('GPIO.'+mode))
        # GPIO.output(gpio['wheel'][wheel + '_reverse'], eval('GPIO.'+ mode))
    if direction == 'reverse':
        time.sleep(0.01)
        GPIO.output(gpio['wheel'][wheel + '_reverse'], eval('GPIO.' + mode))


def __forward():
    '''Move left wheel forward.'''
    print('forward start')
    __robo_wheel_control('left', 'forward', 'HIGH')
    __robo_wheel_control('right', 'forward', 'HIGH')

    #__robo_wheel_control('left', 'forward', 'LOW')
    #__robo_wheel_control('right', 'forward', 'LOW')
    print('forward end')


def __reverse():
    '''Move left wheel forward.'''
    print('reverse start')
    __robo_wheel_control('left', 'reverse', 'HIGH')
    __robo_wheel_control('right', 'reverse', 'HIGH')

    # time.sleep(3)

    #__robo_wheel_control('left', 'reverse', 'LOW')
    #__robo_wheel_control('right', 'reverse', 'LOW')
    print('reverse stop')


def __stop():
    print('stop start')
    __robo_wheel_control('left', 'forward', 'LOW')
    __robo_wheel_control('right', 'forward', 'LOW')
    __robo_wheel_control('left', 'reverse', 'LOW')
    __robo_wheel_control('right', 'reverse', 'LOW')
    print('stop stop')


def __left_turn():
    '''Move robo left.'''
    __robo_wheel_control('left', 'reverse', 'HIGH')
    __robo_wheel_control('right', 'forward', 'HIGH')


def __right_turn():
    '''Move robo right.'''
    __robo_wheel_control('left', 'forward', 'HIGH')
    __robo_wheel_control('right', 'reverse', 'HIGH')


def detect_obstacle_dist():
    '''Calculate the distance of obstacle.'''
    front_pwm = GPIO.PWM(gpio['servo']['front_trigger'], 50)
    front_pwm.start(2.5)  # set servo to 0 degree.
    control = threshold['servo_cycle']
    try:
        while True:
            angle_history = []
            for angle in range(len(control)):
                front_pwm.ChangeDutyCycle(control[angle])
                time.sleep(0.5)
                dist = __get_distance()
                angle_history.append(dist)
                # if dist < threshold['critical_dist']:
                #     __stop()
                if dist > threshold['min_stop_dist']:
                    if angle == 1:
                        # center lline
                        __forward()
                    # else:
                    #     __stop()
                    #     print("do something here")
                        # print("if", dist, angle_history)
                    elif angle == 2:
                        if angle_history[0] > angle_history[1]:
                            # can go right
                            # print("right")
                            __right_turn()
                            time.sleep(1)
                            __stop()
                        elif angle_history[2] > angle_history[1]:
                            # can go left
                            # print("left")
                            __left_turn()
                            time.sleep(1)
                            __stop()
                        # else:
                        # print(max(angle_history), angle_history)
                else:
                    __stop()
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


def robo_init():
    '''Init the robo GPIO conf and get ready for action.'''
    GPIO.setmode(GPIO.BCM)

    # servo setup
    GPIO.setup(gpio['servo']['front_trigger'], GPIO.OUT)  # front

    # setup Ultrasonic Sensors
    GPIO.setup(gpio['ultrasensor']['front_trigger'], GPIO.OUT)
    GPIO.setup(gpio['ultrasensor']['front_echo'], GPIO.IN)

    GPIO.setup(gpio['wheel']['left_forward'], GPIO.OUT)
    GPIO.setup(gpio['wheel']['right_forward'], GPIO.OUT)
    GPIO.setup(gpio['wheel']['left_reverse'], GPIO.OUT)
    GPIO.setup(gpio['wheel']['right_reverse'], GPIO.OUT)
