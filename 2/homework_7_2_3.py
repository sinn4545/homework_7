import RPi.GPIO as GPIO
import time

BUZZER = 12
SW1 = 5
preSWValue = 0

'''     C4   D4   E4   F4   G4   A4   B4   C5'''
freq = [262, 294, 330, 349, 392, 440, 494, 523]
freq_time = [0.5, 0.125, 0.01]

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER, GPIO.OUT)

GPIO.setup(SW1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

p = GPIO.PWM(BUZZER, freq[1])

def honk() :
    # C4 C4
    p.start(50)
    p.ChangeFrequency(262)
    time.sleep(freq_time[0])
    p.stop()

    time.sleep(freq_time[2])

    p.start(50)
    p.ChangeFrequency(262)
    time.sleep(freq_time[1])

    # E4 E4
    p.ChangeFrequency(330)
    time.sleep(freq_time[0])
    p.stop()
    
    time.sleep(freq_time[2])

    p.start(50)
    p.ChangeFrequency(330)
    time.sleep(freq_time[1])

    # A3 A3
    p.ChangeFrequency(220)
    time.sleep(freq_time[0])
    p.stop()
    
    time.sleep(freq_time[2])

    p.start(50)
    p.ChangeFrequency(220)
    time.sleep(freq_time[1])

    # C4 C4
    p.ChangeFrequency(262)
    time.sleep(freq_time[0])
    p.stop()
    
    time.sleep(freq_time[2])

    p.start(50)
    p.ChangeFrequency(262)
    time.sleep(freq_time[1])

    # D4 D4
    p.ChangeFrequency(294)
    time.sleep(freq_time[0])
    p.stop()
    
    time.sleep(freq_time[2])

    p.start(50)
    p.ChangeFrequency(294)
    time.sleep(freq_time[1])

    # F4 F4
    p.ChangeFrequency(349)
    time.sleep(freq_time[0])
    p.stop()
    
    time.sleep(freq_time[2])

    p.start(50)
    p.ChangeFrequency(349)
    time.sleep(freq_time[1])

    # G3 G3
    p.ChangeFrequency(196)
    time.sleep(freq_time[0])
    p.stop()
    
    time.sleep(freq_time[2])

    p.start(50)
    p.ChangeFrequency(196)
    time.sleep(freq_time[1])

    # B3 B3
    p.ChangeFrequency(247)
    time.sleep(freq_time[0])
    p.stop()
    
    time.sleep(freq_time[2])

    p.start(50)
    p.ChangeFrequency(247)
    time.sleep(freq_time[1])
    p.stop()

try :
    while True :
        swValue = GPIO.input(SW1)

        if preSWValue == 0 and swValue == 1:
            honk()
            preSWValue = swValue
        
        elif preSWValue == 1 and swValue == 0 :
            preSWValue = swValue

        time.sleep(0.1)
except KeyboardInterrupt :
    pass

p.stop()
GPIO.cleanup()
