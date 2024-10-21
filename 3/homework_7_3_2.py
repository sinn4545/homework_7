import RPi.GPIO as GPIO
import time

PWM = [ 18, 23 ]
AIN = [ 22, 27 ]
BIN = [ 25, 24 ]

SW = [5, 6, 13, 19]
preSWValue = [0, 0, 0, 0]
direction = ['앞', '오른쪽', '왼쪽', '뒤']

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

for i in SW:
    GPIO.setup(i, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

for i in range(0, 2) :
    GPIO.setup(PWM[i], GPIO.OUT)
    GPIO.setup(AIN[i], GPIO.OUT)
    GPIO.setup(BIN[i], GPIO.OUT)


L_Motor = GPIO.PWM(PWM[0], 500)
L_Motor.start(0)
R_Motor = GPIO.PWM(PWM[1], 500)
R_Motor.start(0)

try :
    while True :
        swValue = [ GPIO.input(SW[0]), GPIO.input(SW[1]), GPIO.input(SW[2]), GPIO.input(SW[3])]
        
        for i in range(0, 4) :
            if preSWValue[i] == 0 and swValue[i] == 1 :
                for j in range(0, 2) :
                    GPIO.output(AIN[j], j if i in [0, 1] else 1 - j)
                    GPIO.output(BIN[j], j if i in [0, 2] else 1 - j)
                    '''
                    if i == 0:
                        GPIO.output(AIN[j], j)
                        GPIO.output(BIN[j], j)

                    elif i == 1:
                        
                        GPIO.output(AIN[j], j)
                        GPIO.output(BIN[j], 1 - j)

                    elif i == 2:
                        GPIO.output(AIN[j], 1 - j)
                        GPIO.output(BIN[j], j)

                    elif i == 3 :
                        GPIO.output(AIN[j], 1 - j)
                        GPIO.output(BIN[j], 1 - j)
                    '''

                L_Motor.ChangeDutyCycle(50)
                R_Motor.ChangeDutyCycle(50)

                print("\"SW", i+1, "click:", direction[i], "\"")
                preSWValue[i] = swValue[i]
            
            elif preSWValue[i] == 1 and swValue[i] == 0 :
                L_Motor.ChangeDutyCycle(0)
                R_Motor.ChangeDutyCycle(0)
                preSWValue[i] = swValue[i]

except KeyboardInterrupt :
    pass

GPIO.cleanup()