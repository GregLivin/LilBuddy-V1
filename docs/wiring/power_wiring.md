\# Lil Buddy V1 Power Wiring



This document explains the power system used by Lil Buddy V1.



The robot uses a \*\*4S LiPo battery (14.8V)\*\* as the main power source and two buck converters to create separate voltage rails.



---



\# Power System Overview



Main Battery  

4S LiPo Battery (14.8V)



Power Rails



14.8V → 5V Buck Converter → Jetson + Logic Electronics



14.8V → 6V Buck Converter → Servo Motors



---



\# Power Architecture Diagram



&nbsp;       4S LiPo Battery (14.8V)

&nbsp;                │

&nbsp;                │

&nbsp;       -------------------------

&nbsp;       │                       │

&nbsp;       │                       │

&nbsp;       ▼                       ▼



&nbsp;  5V Buck Converter      6V Buck Converter

&nbsp;       │                       │

&nbsp;       │                       │

&nbsp;       ▼                       ▼



&nbsp;Jetson Orin Nano          PCA9685 Servo Rail

&nbsp;Cameras                   Servo Motors

&nbsp;Display                   DS3218 Servos





Jetson Power



The Jetson Orin Nano requires stable 5V power.



Recommended wiring:



Battery → 5V Buck Converter → Jetson DC input



This rail powers:



Jetson Orin Nano



Cameras



Display



Microphone



Speaker



Servo Power



Servo motors require higher current than the Jetson can supply.



Servos must NOT be powered from the Jetson.



Battery → 6V Buck Converter → PCA9685 V+



This rail powers:



DS3218 Shoulder Servos



Elbow Servos



Wrist Servos



Neck Servo



PCA9685 Wiring



Jetson communicates with the PCA9685 using the I2C bus.



Connections:



Jetson SDA → PCA9685 SDA

Jetson SCL → PCA9685 SCL



Jetson GND → PCA9685 GND



Important:



All grounds must be connected together.



Jetson GND

Battery GND

Servo Rail GND



Important Safety Rules



Never power servos directly from the Jetson.



Servos can draw several amps and will cause the Jetson to reset or shut down.



Always use a dedicated servo power rail.



Recommended Voltage Rails



5V Rail



Jetson

Display

Cameras

Sensors



6V Rail



PCA9685

All Servo Motors



Future Power Expansion



Later versions of Lil Buddy may include:



larger battery packs



power distribution boards



voltage monitoring



automatic shutdown systems





