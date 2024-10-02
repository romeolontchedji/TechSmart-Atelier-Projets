from servo import Servo
import time

servo = Servo(14)
while 1 :
    for i in range(180):
        servo.write_angle(i)
        time.sleep_ms(10)

    for i in range(180,0,-1):
        servo.write_angle(i)
        time.sleep_ms(10)
    


