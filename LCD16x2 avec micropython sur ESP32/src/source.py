from i2c_lcd import I2cLcd
from machine import I2C,Pin
import time

address = 0x27
i2c = I2C(scl=Pin(22),sda=Pin(21),freq=400000)
lcd = I2cLcd(i2c,address,2,16)

lcd.display_on()
lcd.backlight_on()
lcd.move_to(0,1)
lcd.putstr("BONJOUR")
    

