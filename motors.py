import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)  # use physical pin numbering
motor1 = 13 # GPIO Pin for motor1
motor2 = 12 # GPIO Pin for motor2
GPIO.setup(motor1, GPIO.OUT)
GPIO.setup(motor2, GPIO.OUT)
motor1Servo = GPIO.PWM(motor1, 1000) # set Motors to PWM. Change this depeneding on how your motor controller works
motor1Servo.start(8)
motor2Servo = GPIO.PWM(motor2, 1000) # set Motors to PWM. Change this depeneding on how your motor controller works
motor2Servo.start(8)
motor1Servo.ChangeDutyCycle(0) # 
motor2Servo.ChangeDutyCycle(0) # RPI can encounter a bug that might require this to be applied twice
duty1 = 5
duty2 = 5

def turn(value): 
    motor1Servo.ChangeDutyCycle(speed * (1 + value)) # 50 Right, 0 Neutral, -50 Left
    motor2Servo.ChangeDutyCycle(speed * (1 - value))
    duty1 = 50 + value
    duty2 = 50 - value
    
def acc(value):
    motor1Servo.ChangeDutyCycle(value)
    motor2Servo.ChangeDutyCycle(value)
    duty1 = value
    duty2 = value
    global speed
    speed = value

def stop():
    motor1Servo.stop()
    motor2Servo.stop()
    
def start():
    motor1Servo.start(duty1)
    motor2Servo.start(duty2)
    
def Left(value):
    motor1Servo.ChangeFrequency(value)
    
def Right(value):
    motor2Servo.ChangeFrequency(value)
