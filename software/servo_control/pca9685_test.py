"""
Lil Buddy V1 - PCA9685 Servo Test (DS3218)

What this does:
- Connects to PCA9685 over I2C
- Moves a servo on a selected channel back and forth

WIRING (quick):
Jetson I2C -> PCA9685:
- SDA -> SDA
- SCL -> SCL
- GND -> GND
- VCC -> 3.3V or 5V logic (match your board; 3.3V is fine)

Servo power (IMPORTANT):
- PCA9685 V+ -> 6V servo rail (NOT Jetson 5V)
- PCA9685 GND must be common with Jetson GND
"""

import time

try:
    from adafruit_servokit import ServoKit
except Exception as e:
    raise SystemExit(
        "Missing library. Install on Jetson with:\n"
        "  python3 -m pip install --upgrade pip\n"
        "  python3 -m pip install adafruit-circuitpython-servokit\n"
        f"\nOriginal error: {e}"
    )

# ----------------------------
# SETTINGS
# ----------------------------
CHANNELS = 16          # PCA9685 channels
SERVO_CH = 0           # change to 0-15
MIN_ANGLE = 10         # keep away from hard stops
MAX_ANGLE = 170
PAUSE_SEC = 1.0

# If your servo jitters, you can try setting pulse width range.
# DS3218 often works well around 500-2500us (varies by servo).
USE_PULSE_TUNING = True
MIN_PULSE = 500
MAX_PULSE = 2500

# ----------------------------
# INIT
# ----------------------------
kit = ServoKit(channels=CHANNELS)

if USE_PULSE_TUNING:
    kit.servo[SERVO_CH].set_pulse_width_range(MIN_PULSE, MAX_PULSE)

print(f"[OK] PCA9685 detected. Testing servo channel {SERVO_CH}...")
print(f"Angles: {MIN_ANGLE} -> 90 -> {MAX_ANGLE}")

# ----------------------------
# LOOP
# ----------------------------
while True:
    kit.servo[SERVO_CH].angle = MIN_ANGLE
    print(f"Angle: {MIN_ANGLE}")
    time.sleep(PAUSE_SEC)

    kit.servo[SERVO_CH].angle = 90
    print("Angle: 90")
    time.sleep(PAUSE_SEC)

    kit.servo[SERVO_CH].angle = MAX_ANGLE
    print(f"Angle: {MAX_ANGLE}")
    time.sleep(PAUSE_SEC)