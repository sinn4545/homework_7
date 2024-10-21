import RPi.GPIO as GPIO
import time

SW1 = 5
preSWValue = 0

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(SW1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


try :
    while True :
        swValue = GPIO.input(SW1)
        
        if preSWValue == 0 and swValue == 1 :
            print("\"click SW1\"")
            preSWValue = swValue
        
        elif preSWValue == 1 and swValue == 0:
            preSWValue = swValue
        time.sleep(0.1)

except KeyboardInterrupt :
    pass

GPIO.cleanup()