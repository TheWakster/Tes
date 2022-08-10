import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

PWR1,ENA1,IN1,IN2,GND = 2,33,31,29,39
GPIO.setup(ENA1, GPIO.OUT)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
PWMA = GPIO.PWM(ENA1,100)
PWMA.start(0)

PWR1,ENA2,IN3,IN4,GND = 4,32,18,16,34
GPIO.setup(ENA2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)
PWMA = GPIO.PWM(ENA2,100)
PWMA.start(0)

PWMA.ChangeDutyCycle(30)
sleep(5)
GPIO.output(IN1,GPIO.HIGH)
sleep(5)
GPIO.output(IN2,GPIO.LOW)

PWMA.ChangeDutyCycle(30)
sleep(5)
GPIO.output(IN3,GPIO.LOW)
sleep(5)
GPIO.output(IN4,GPIO.HIGH)

GPIO.cleanup()
