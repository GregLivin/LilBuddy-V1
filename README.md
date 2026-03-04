# Lil Buddy V1 🤖

Lil Buddy V1 is a modular humanoid AI robot designed and built by student engineers.

The project focuses on creating a robotics platform capable of vision, voice interaction, and physical movement using high torque servo motors and AI computing hardware.

Lil Buddy is designed as an expandable robotics system that can evolve into multiple specialized robots for different applications.

Possible applications include:

• Robotics engineering education  
• AI assistant robots  
• Healthcare assistant robots  
• Cybersecurity monitoring robots  
• Smart home robotics systems  

---

# Robot Overview

Lil Buddy V1 is a **24 inch humanoid robot** powered by an **NVIDIA Jetson Orin Nano AI computer**.

The robot includes:

• AI vision system  
• Voice interaction  
• Dual camera "eyes"  
• Moving robotic arms  
• Chest display interface  
• Modular electronics architecture  

Future versions will include **walking legs and advanced autonomy**.

---

# Core Hardware

### AI Computer
NVIDIA Jetson Orin Nano

### Servo Control
PCA9685 16-Channel PWM Servo Driver

### Servo Motors
DS3218 High Torque Digital Servos

### Power System
4S LiPo Battery (14.8V)

Power rails:

• 14.8V → 5V buck converter (Jetson and logic electronics)  
• 14.8V → 6V buck converter (servo power rail)

### Display
10.1" LCD HDMI touchscreen mounted in the chest

### Vision System
Dual cameras mounted inside the robot head

### Audio System
Internal speaker system for voice output

### Robot Structure
3D printed components designed in **Autodesk Fusion 360**

Printed using **Bambu Lab P1S 3D Printer**

---

# Robot Dimensions

Total Height  
24 inches (610 mm)

### Torso

Width: 220 mm  
Height: 300 mm  
Depth: 110 mm  

### Head

Height: ~150 mm  
Eye spacing: 60–70 mm  

### Arm Structure

Upper Arm: 80 mm  
Forearm: 80 mm  
Hand: 50 mm  

Total Arm Reach: ~210 mm

### Shoulder System

2 Degrees of Freedom

• Forward / Back swing  
• Arm lift up / down  

---

# Repository Structure

docs/blueprints/system_architecture.md
Robot hardware and software architecture diagram

LilBuddy-V1

cad
Fusion 360 designs, STL files, STEP files and mechanical drawings

docs
Engineering documentation, blueprints and build notes

electronics
Wiring diagrams and schematics

hardware
Mechanical assembly information

software
Robot control software and AI modules

media
Images and videos of the robot

---

---

# Software Modules

### Jetson Control
Jetson system configuration and robotics runtime environment

### Servo Control
PWM control system using PCA9685

### Vision System
Computer vision using AI models and cameras

### Voice System
Speech recognition and voice synthesis

### User Interface
Robot display interface and system status display

---

# Development Roadmap

### Version 1

• Functional humanoid upper body  
• AI vision system  
• Voice interaction  
• Moving robotic arms  
• Chest display interface  

### Version 2

• Walking humanoid robot  
• Balance and locomotion control  

### Version 3

• Fully autonomous AI assistant robot

---

# 3D Printed Components

Lil Buddy V1 is designed in **Autodesk Fusion 360** and printed using a **Bambu Lab P1S 3D Printer**.

The robot uses a **modular design** so components can be upgraded or replaced easily.

---

## Body Structure

1. Head shell – outer robot head housing  
2. Head back cover – removable access panel  
3. Camera eye mounts – holds dual cameras  
4. Neck turret base – rotating base between head and torso  
5. Neck servo mount – bracket for neck servo  

---

## Torso Assembly

6. Torso front shell – chest housing with display opening  
7. Torso rear cover – removable electronics access panel  
8. Chest display frame – mount for 10.1" display  
9. Jetson mounting plate – mount for Jetson Orin Nano  
10. Battery tray – holder for LiPo battery  
11. Speaker mount – internal audio mount  

---

## Shoulder System

12. Left shoulder turret base  
13. Right shoulder turret base  
14. Shoulder bearing support housing  
15. Shoulder servo mount bracket  
16. Shoulder outer shell cover  

---

## Arm Assembly

17. Upper arm shell (left)  
18. Upper arm shell (right)  
19. Elbow joint bracket  
20. Forearm shell (left)  
21. Forearm shell (right)  
22. Wrist servo mount  
23. Robot hand base plate  
24. Finger mount bracket (optional gripper)

---

## Internal Electronics Mounts

25. PCA9685 mounting plate  
26. Buck converter mounting bracket  
27. Power distribution mount  
28. Wire routing clips  
29. Cooling fan mount  
30. Cable management bracket  

---

## Future Expansion (V2 Legs)

31. Hip interface mount plate  
32. Hip servo mount brackets  
33. Upper leg housing  
34. Knee joint bracket  
35. Lower leg housing  
36. Foot base plate  

Estimated printed parts for Lil Buddy V1 upper body: **~30 parts**

Estimated printed parts for full humanoid version: **~36–40 parts**

---

# Hardware Platform Philosophy

Lil Buddy V1 is designed using a **modular robotics architecture**.

This allows the robot to be upgraded without redesigning the entire system.

The platform is ideal for:

• Robotics research  
• Engineering education  
• AI experimentation  
• Rapid prototyping  

---

# Project Vision

Lil Buddy represents the beginning of a larger robotics ecosystem focused on accessible AI robotics development.

The long-term goal is to create:

• Specialized AI robots  
• Open robotics education platforms  
• Modular robotics kits  

---

# License

MIT License

---

# Author

Gregory Livingston  
Robotics Engineering Student  
Houston Community College

Project: **Lil Buddy Robotics**
