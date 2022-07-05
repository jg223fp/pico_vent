from machine import Pin
import time
import utime
from dht import DHT11, InvalidChecksum

#pin setup
red_led = Pin(0, Pin.OUT)
sensor_pin = Pin(27, Pin.OUT, Pin.PULL_DOWN)

#init values
red_led.value(0)

#Functions
def blink_red():
    print("Red LED flashing...")
    for i in range(8):
        red_led.toggle()
        time.sleep(0.2)  

#Main
while True:  
    #blink_red()
    utime.sleep(1)
    sensor = DHT11(sensor_pin)
    t  = (sensor.temperature)
    h = (sensor.humidity)
    print("Temperature: {}".format(sensor.temperature))
    print("Humidity: {}".format(sensor.humidity))
    time.sleep(1)
             

    
    