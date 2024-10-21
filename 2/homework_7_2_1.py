import RPi.GPIO as GPIO
import time

BUZZER = 12

'''      C4   D4   E4   F4   G4   A4   B4   C5      '''
freq = [ 262, 294, 330, 349, 392, 440, 494, 523 ]

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER, GPIO.OUT)

p = GPIO.PWM(BUZZER, freq[0])
p.start(50)

try :
    while True :
        p.start(50)
        for i in range(0, 8) :
            p.ChangeFrequency(freq[i])
            time.sleep(0.3)
        p.stop()
        time.sleep(0.1)
except KeyboardInterrupt :
    pass

p.stop()
GPIO.cleanup()