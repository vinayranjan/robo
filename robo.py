"""Main control file of the robo."""

import time
import RPi.GPIO as GPIO
from config import gpio
import utils

if __name__ == '__main__':
    utils.robo_init()
    # utils.detect_obstacle_dist()
    utils.__robo_wheel_control('left', 'forward', 'HIGH')
    utils.__robo_wheel_control('right', 'forward', 'HIGH')
    time.sleep(1)
    utils.__robo_wheel_control('left', 'forward', 'LOW')
    utils.__robo_wheel_control('right', 'forward', 'LOW')