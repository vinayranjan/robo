# servo responsible for rotating ultrasonic sersors
gpio = {
    'servo': {
        'front_trigger': 17,
        'back_trigger': 0 # to be defined later
    },

    # motors responsible for moving the robo
    'wheel': {
        'left_reverse': 26,
        'left_forward': 20,
        'right_reverse': 16,
        'right_forward': 19
    },
    # sensors responsible for obstacle detection
    'ultrasensor': {
        'front_trigger': 18,
        'front_echo': 24,
        'reverse_trigger': 0 # to be defined later 
    }
}

threshold = {
    'critical_dist': 25,
    'min_stop_dist': 60,
    'approach_dist': 60,
    'servo_cycle': [5, 7.5, 10],
}

