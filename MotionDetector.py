from machine import Pin
import time

data = Pin(16)
print(data.value())

read = 0
wait = 0

while data.value() == 1:
    print("Warte auf Bewegung")

while True:
    read = data.value()
    if read == 1 and wait == 0:
        print("Alarm, Alarm")
        wait = 1

    elif read == 0 and wait == 1:
        print("Warte auf Bewegung")
        wait = 0

    time.sleep(0.1)