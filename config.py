# servo responsible for rotating ultrasonic sersors
gpio = {
'servo': {
    'front_trigger': 11,
    'reverse_trigger': 0 # to be defined later
},

# motors responsible for moving the robo
'motor': {
    'left_forward': 26,
    'left_reverse': 20,
    'right_forward': 16,
    'right_reverse': 19   
},
# sensors responsible for obstacle detection
'ultrasensor': {
    'front_trigger': 18,
    'front_echo': 24,
    'reverse_trigger': 0, # to be defined later
    'reverse_trigger': 0 # to be defined later 
}
}

