from machine import Pin
import time
import utime
from dht import DHT11, InvalidChecksum

#pin setup
red_led = Pin(0, Pin.OUT)
sensor_pin = Pin(27, Pin.OUT, Pin.PULL_DOWN)

#init values
red_led.value(0)
sensor = DHT11(sensor_pin)

#Functions
def boot():
    """Runs a small test for the sensor and for the motor,
        Flashes the red LED to indicate success. If the lifght is solid an error has accured.
    """
    print("System started")
    print("Performing tests")
    test_sensor()
    test_motor()
    print("Tests completed")
    for i in range(6):
        red_led.toggle()
        time.sleep(0.1)
        
def test_motor():
    """Performs a test for the fan
    """
    pass

def test_sensor():
    """Performs a test for the DHT11 sensor.
        Temperature limits: 0 to 50 C
        Humidity limits: 20-80 +-5%
        Max update frequenzy: 1 Hz
    """
    t = get_temp()
    if t < 0 or t > 50: 
        print("ERROR: Temperature out of range")
        error()
    h = get_humidity()
    if h < 15 or h > 95:  
        print("ERROR: Humidity out of range")
        error()

def error():
    """If an error accours the red LED is turned on with a solid light.
    """
    red_led.value(1)
    while True:
        pass
    
def blink_red():
    """Flashes the red LED 2 times.
    """
    print("Red LED flashing...")
    for i in range(4):
        red_led.toggle()
        time.sleep(0.5)
        
def get_temp():
    """Returns a temperature value from the sensor.
    """
    return sensor.temperature

def get_humidity():
    """Returns a humidity value from the sensor.
    """
    return sensor.humidity

    
#Main
boot()
print("Starting main program...")
while True:  
    utime.sleep(1)
    print("Humidity: {}".format(get_humidity()))
    utime.sleep(1)
             

    
    