#Importing needed libs for this project
import time
from machine import Pin
from dht import DHT # https://github.com/JurassicPork/DHT_PyCom


#Calls function DHT with arguments and assigns returned values to variable th
th = DHT(Pin('P23', mode=Pin.OPEN_DRAIN), 0)
#Variable value is used as a counter later
value = 1
time.sleep(2)


#While loop gives 'result' values by using function th.read()
while True:
    result = th.read()
    while not result.is_valid():
        time.sleep(.5)
        result = th.read()

    #Prints the measurement results into cli. Added easy checkup of how many measurements that's been done
    print('Measurement nr :' + str(value))
    print('Temp:', result.temperature)
    print('RH:', result.humidity)
    
    #Adds +1 for each loop.
    value += 1

    #Sends the values seen in cli to the pybytes.io server
    pybytes.send_signal(1,result.temperature)
    pybytes.send_signal(2,result.humidity)

    #Waits for 1800 sec == 30 minutes before beginning loop another time
    time.sleep(1800)
