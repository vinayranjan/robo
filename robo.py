"""Main control file of the robo."""

import time
import RPi.GPIO as GPIO
from config import gpio
import utils


def move_forward():
    utils.__robo_wheel_control('left', 'forward', 'HIGH')
    utils.__robo_wheel_control('right', 'forward', 'HIGH')
    time.sleep(1)
    utils.__robo_wheel_control('left', 'forward', 'LOW')
    utils.__robo_wheel_control('right', 'forward', 'LOW')


def move_reverse():
    utils.__robo_wheel_control('left', 'reverse', 'HIGH')
    utils.__robo_wheel_control('right', 'reverse', 'HIGH')
    time.sleep(1)
    utils.__robo_wheel_control('left', 'reverse', 'LOW')
    utils.__robo_wheel_control('right', 'reverse', 'LOW')

if __name__ == '__main__':
    
    # utils.detect_obstacle_dist()
    utils.robo_init()
    move_forward()
    move_reverse()
    GPIO.cleanup()