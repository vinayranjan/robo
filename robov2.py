import sys
import time
import RPi.GPIO as GPIO

mode=GPIO.getmode()

GPIO.cleanup()


Forward=26
LP=26
RP=16

Backward=20
LM=20
RM=19
sleeptime=1

#GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM)

GPIO.setup(LP, GPIO.OUT)
GPIO.setup(LM, GPIO.OUT)
GPIO.setup(RP, GPIO.OUT)
GPIO.setup(RM, GPIO.OUT)
def forward_high():
        GPIO.output(LP, GPIO.HIGH)
        GPIO.output(RP,GPIO.HIGH)
        print("Moving Forward")

def forward_low():
        GPIO.output(LP,GPIO.LOW)
        GPIO.output(RP, GPIO.LOW)

def reverse(x):
        GPIO.output(LM, GPIO.HIGH)
        GPIO.output(RM, GPIO.HIGH)
        print("Moving Backward")
        time.sleep(x)

        GPIO.output(LM, GPIO.LOW)
        GPIO.output(RM,GPIO.LOW)

#while (1):
#        forward(2)
#        reverse(2)
#        GPIO.cleanup()


# sensor

GPIO_TRIGGER = 18
GPIO_ECHO = 24

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
 
def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance

if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            time.sleep(0.3)
            if dist < 5:
                print("I am in extreme near block", dist)
                GPIO.cleanup()
                exit()
            if dist > 40:
                forward_high()
                print("I am in high if block", dist)
            else:
                print("I am in low else block", dist)
                forward_low()
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()

