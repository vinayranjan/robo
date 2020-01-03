"""Main control file of the robo."""

import time
import RPi.GPIO as GPIO
from config import gpio
import utils

if __name__ == '__main__':
    utils.robo_init()
    utils.detect_obstacle_dist()