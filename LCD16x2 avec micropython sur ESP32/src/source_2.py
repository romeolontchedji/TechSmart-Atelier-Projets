from i2c_lcd import I2cLcd
from machine import SoftI2C, Pin
import time

# Configuration de l'I2C et de l'écran LCD
address = 0x27
i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=400000)
lcd = I2cLcd(i2c, address, 2, 16)

lcd.display_on()  # Allume l'écran d'affichage
lcd.backlight_on()  # Active le rétroéclairage

# Message à afficher
message = "ABONNEZ VOUS A LA CHAINE SVP "

# Défilement du message
while True:
    for i in range(len(message) - 15):
        lcd.move_to(0, 0)  # Déplacement sur la première ligne
        # Affichage d'une sous-chaîne du message de longueur 16 caractères
        lcd.putstr(message[i:i + 16])
        time.sleep(1)  # Pause pour l'effet de défilement





