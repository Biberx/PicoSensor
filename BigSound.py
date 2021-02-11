from machine import Pin, ADC
import time

digital = Pin(16)

while True:
        if digital.value() == 1:
            print("Sound")
            time.sleep(1)


    