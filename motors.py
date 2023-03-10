import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)  # use broadcom pin numbering (not board pin numbering)

# setup
# motor control pins
motorL = 13 # GPIO Pin for motorL # previously motor1
motorR = 12 # GPIO Pin for motorR # previously motorR
GPIO.setup(motorL, GPIO.OUT)
GPIO.setup(motorR, GPIO.OUT)

# reverse control pins
reverseL = 5 # pin for reverse left
reverseR = 6 # pin for reverse right
GPIO.setup(reverseL, GPIO.OUT)
GPIO.setup(reverseR, GPIO.OUT)
GPIO.output(reverseL, False) # set so no pin output, aka go forwards
GPIO.output(reverseR, False) # set so no pin output, aka go forwards

motorLServo = GPIO.PWM(motorL, 1000) # set Motors to PWM. Change this depeneding on how your motor controller works
motorLServo.start(8)
motorRServo = GPIO.PWM(motorR, 1000) # set Motors to PWM. Change this depeneding on how your motor controller works
motorRServo.start(8)
motorLServo.ChangeDutyCycle(0) # 
motorRServo.ChangeDutyCycle(0) # RPI can encounter a bug that might require this to be applied twice
duty1 = 5
duty2 = 5

isReversed = False

def turn(value): 
    motorLServo.ChangeDutyCycle(speed * (1 + value)) # 50 Right, 0 Neutral, -50 Left
    motorRServo.ChangeDutyCycle(speed * (1 - value))
    duty1 = 50 + value
    duty2 = 50 - value
    
def acc(value):
    # check for is reversed
     
    motorLServo.ChangeDutyCycle(value)
    motorRServo.ChangeDutyCycle(value)
    duty1 = value
    duty2 = value
    global speed
    speed = value

def stop():
    motorLServo.stop()
    motorRServo.stop()
    
def start():
    motorLServo.start(duty1)
    motorRServo.start(duty2)
    
def Left(value):
    motorLServo.ChangeFrequency(value)
    
def Right(value):
    motorRServo.ChangeFrequency(value)

def setReverse(isRev):
    global isReversed
    if isReversed == isRev:
        return
    isReversed = isRev
    GPIO.output(reverseL, isRev)
    GPIO.output(reverseR, isRev)