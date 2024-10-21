import RPi.GPIO as GPIO
import time

BUZZER = 12
SW = [5, 6, 13, 19]

'''
       SW2
   SW1  ●  SW4
    ●       ●
        ●
       SW3
'''

preSWValue = [0, 0, 0, 0]

'''     C4   D4   E4   F4   G4   A4   A4#  B4  C5'''
freq = [262, 294, 330, 349, 392, 440, 466, 494, 523]

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER, GPIO.OUT)

for i in SW:
    GPIO.setup(i, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

p = GPIO.PWM(BUZZER, freq[1])

try :
    while True :
        swValue = [ GPIO.input(SW[0]), GPIO.input(SW[1]), GPIO.input(SW[2]), GPIO.input(SW[3])]

        if swValue[1] == 1 and swValue[3] == 1:
            p.start(50)
            p.ChangeFrequency(freq[8])

        elif swValue[2] == 1 and swValue[3] == 1 :
            p.start(50)
            p.ChangeFrequency(freq[6])

        elif swValue[0] == 1 and swValue[3] == 1 :
            p.start(50)
            p.ChangeFrequency(freq[7])

        elif swValue[0] == 1 and swValue[2] == 1 :
            p.start(50)
            p.ChangeFrequency(freq[5])

        elif swValue[0] == 1 and swValue[1] == 1 :
            p.start(50)
            p.ChangeFrequency(freq[4])

        elif swValue[3] == 1 :
            p.start(50)
            p.ChangeFrequency(freq[3])

        elif swValue[2] == 1 :
            p.start(50)
            p.ChangeFrequency(freq[2])

        elif swValue[1] == 1 :
            p.start(50)
            p.ChangeFrequency(freq[1])
        
        elif swValue[0] == 1 :
            p.start(50)
            p.ChangeFrequency(freq[0])

        else :
            p.stop()
        
except KeyboardInterrupt :
    pass

p.stop()
GPIO.cleanup()