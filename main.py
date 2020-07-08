import time
from machine import Pin
from dht import DHT # https://github.com/JurassicPork/DHT_PyCom

# Type 0 = dht11
# Type 1 = dht22

th = DHT(Pin('P23', mode=Pin.OPEN_DRAIN), 0)
value = 1
time.sleep(2)


while True:
    result = th.read()
    while not result.is_valid():
        time.sleep(.5)
        result = th.read()

    print('Mätvärde nr :' + str(value))
    print('Temp:', result.temperature)
    print('RH:', result.humidity)
    value += 1

    pybytes.send_signal(1,result.temperature)
    pybytes.send_signal(2,result.humidity)

    time.sleep(1800)
