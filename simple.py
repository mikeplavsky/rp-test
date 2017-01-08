import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)

on = lambda: GPIO.output(7, True)
off = lambda: GPIO.output(7, False)
done = lambda: GPIO.cleanup()
