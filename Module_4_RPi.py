import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

ledPin = 11
buttonPin = 15

GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down = GPIO.PUD_UP)

while True:
    try:
        if GPIO.input(buttonPin) == False:
            GPIO.output(ledPin, GPIO.LOW)
            time.sleep(1)
            GPIO.output(ledPin, GPIO.HIGH)
            time.sleep(1)
            print('Button not pressed')
        elif GPIO.input(buttonPin) == True:
            GPIO.output(ledPin, GPIO.HIGH)
            print('Button pressed')
    except KeyboardInterrupt:
        GPIO.cleanup()
        print('\n STOPPED')
        exit()
