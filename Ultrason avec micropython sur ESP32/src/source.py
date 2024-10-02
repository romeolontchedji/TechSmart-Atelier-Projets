from hcsr04 import HCSR04
import time

sensor = HCSR04(trigger_pin=27,echo_pin=26)

while True:
    distance = sensor.distance_mm()
    print(distance)
    time.sleep_ms(500)
    

