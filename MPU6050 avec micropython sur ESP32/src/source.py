from MPU6050 import MPU6050
from machine import Pin

mpu = MPU6050()

# Accelerometer
linear_accel = mpu.read_accel_data() #  [ms^-2]
aX = linear_accel["x"]
aY = linear_accel["y"]
aZ = linear_accel["z"]
print("\n Acceleration linéaire")
print("x: ", aX, " y: ", aY, " z: ", aZ, "\n")


# Gyroscope 
print(" Acceleration angulaire")
angular_accel = mpu.read_gyro_data()   # [deg/s]
gX = angular_accel["x"]
gY = angular_accel["y"]
gZ = angular_accel["z"]
print("x:", gX, " y:", gY, " z:", gZ)





