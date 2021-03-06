from machine import Pin
import time
import utime
from dht import DHT11, InvalidChecksum
import PicoMotorDriver

time.sleep(2)  #Needed to let pico init otherwise it wont boot when on batteries

#pin setup
red_led = Pin(0, Pin.OUT)
sensor_pin = Pin(27, Pin.OUT, Pin.PULL_DOWN)

#init values
red_led.value(0)
sensor = DHT11(sensor_pin)
board = PicoMotorDriver.KitronikPicoMotor()
HUMID_LIMIT = 55

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
    """Performs a test for the fan by spoinning it 100% in 3 s.
    """
    board.motorOn(1, "f", 100)
    time.sleep(3)
    board.motorOff(1)
   

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
    
def led_standby():
    """Flashes the red LED 2 times.
    """
    print("Red LED flashing...")
    for i in range(2):
        red_led.toggle()
        time.sleep(0.05)
        
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
    humidity = get_humidity()
    print("Humidity: {}".format(humidity))
    
    if humidity > HUMID_LIMIT:
        print("Motor on")
        board.motorOn(1, "f", 100)
        time.sleep(5)
    else:
        print("Motor off")
        board.motorOff(1)
        
    #time.sleep(10)
    led_standby()
             

    



