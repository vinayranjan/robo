"""Main control file of the robo."""

import time
import RPi.GPIO as GPIO
from config import gpio
import utils


if __name__ == '__main__':
    utils.robo_init()
    #utils.detect_obstacle_dist()

    utils.__forward()
    time.sleep(3)
    utils.__robo_stop()

    utils.__left_turn()
    time.sleep(3)
    utils.__robo_stop()

    utils.__right_turn()
    time.sleep(3)
    utils.__robo_stop()

    utils.__reverse()
    time.sleep(3)
    ˛¸˛	utils.__robo_stop()

    GPIO.cleanup()
