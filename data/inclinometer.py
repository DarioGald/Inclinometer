
import time
from math import atan2, degrees
import board
import adafruit_mpu6050

i2c = board.I2C() 
sensor = adafruit_mpu6050.MPU6050(i2c)
s = time.gmtime()

# Given a point (x, y) return the angle of that point relative to x axis.
# Returns: angle in degrees


def vector_2_degrees(x, y):
    angle = degrees(atan2(y, x))
    if angle < 0:
        angle += 360
    return angle


# Given an accelerometer sensor object return the inclination angles of X/Z and Y/Z
# Returns: tuple containing the two angles in degrees

#print("XZ angle = {:6.2f}deg   YZ angle = {:6.2f}deg, ".format(angle_xz, angle_yz))

def get_inclination(_sensor):
    x, y, z = _sensor.acceleration
    return vector_2_degrees(x, z), vector_2_degrees(y, z)


while True:
    angle_xz, angle_yz = get_inclination(sensor)
    print("{:.2f},{:.2f}".format(angle_xz, angle_yz))
    time.sleep(2)
