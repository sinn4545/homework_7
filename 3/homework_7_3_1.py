import RPi.GPIO as GPIO
import time

PWM = [ 18, 23 ]
AIN = [ 22, 27 ]
BIN = [ 25, 24 ]


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

for i in range(0, 2) :
    GPIO.setup(PWM[i], GPIO.OUT)
    GPIO.setup(AIN[i], GPIO.OUT)
    GPIO.setup(BIN[i], GPIO.OUT)


L_Motor = GPIO.PWM(PWM[0], 500)
L_Motor.start(0)
R_Motor = GPIO.PWM(PWM[1], 500)
R_Motor.start(0)

try :
    for i in range(0, 2) :
        GPIO.output(AIN[i], i)
        GPIO.output(BIN[i], i)
    
    while True :
        L_Motor.ChangeDutyCycle(50)
        R_Motor.ChangeDutyCycle(50)
        time.sleep(1.0)

        L_Motor.ChangeDutyCycle(0)
        R_Motor.ChangeDutyCycle(0)
        time.sleep(1.0)

except KeyboardInterrupt :
    pass

GPIO.cleanup()