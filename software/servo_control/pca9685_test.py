from adafruit_servokit import ServoKit
import time

# PCA9685 has 16 channels
kit = ServoKit(channels=16)

# Move servo on channel 0
while True:
    print("Moving servo to 0°")
    kit.servo[0].angle = 0
    time.sleep(2)

    print("Moving servo to 90°")
    kit.servo[0].angle = 90
    time.sleep(2)

    print("Moving servo to 180°")
    kit.servo[0].angle = 180
    time.sleep(2)