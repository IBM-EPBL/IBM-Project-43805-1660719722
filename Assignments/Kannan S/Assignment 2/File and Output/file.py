import random 
import time

while True:
    temperature = random.randint(1,100)
    humidity = random.randint(1,100)
    print("Temperature: ", temperature)
    print("Humidity: ", humidity)
    if temperature >= 60 and (30 < humidity > 60):
        print("Alarm ON!")
        
    else:
        print("Alarm OFF!")
    
    time.sleep(2)

