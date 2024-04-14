import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)

try:
    while 1:
        print("setez pe unu")
        GPIO.output(11,1)
        time.sleep(5)
        print("setez pe zero")
        GPIO.output(11,0)
        time.sleep(2)
except Exception as e:
    print("coaie : ",e)
finally:
    GPIO.cleanup()