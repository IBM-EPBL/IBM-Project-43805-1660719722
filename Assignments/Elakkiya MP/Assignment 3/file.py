import RPi.GPIO as GPIO 
from time import sleep 

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)


while True: 
    print("LED & Traffic lights ON!")
    GPIO.output(8, GPIO.HIGH) 
    sleep(2) 
    print("LED & Traffic lights OFF!")
    GPIO.output(8, GPIO.LOW) 
    sleep(2) 
    
