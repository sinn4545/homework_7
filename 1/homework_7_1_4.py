import RPi.GPIO as GPIO
import time

SW = [5, 6, 13, 19]
preSWValue = [0, 0, 0, 0]
count = [0, 0, 0, 0]

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

for i in SW:
    GPIO.setup(i, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try :
    while True :
        swValue = [ GPIO.input(SW[0]), GPIO.input(SW[1]), GPIO.input(SW[2]), GPIO.input(SW[3])]
        
        for i in range(0, 4) :
            if preSWValue[i] == 0 and swValue[i] == 1 :
                count[i] = count[i] + 1
                print("('SW", i+1, "click', ", count[i], ')')
                preSWValue[i] = swValue[i]
            
            elif preSWValue[i] == 1 and swValue[i] == 0:
                preSWValue[i] = swValue[i]
        time.sleep(0.1)

except KeyboardInterrupt :
    pass

GPIO.cleanup()