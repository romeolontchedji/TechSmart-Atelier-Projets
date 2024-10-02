from machine import Pin
import time

led = Pin(4,Pin.OUT)

led.on()
time.sleep(1)
led.off()
