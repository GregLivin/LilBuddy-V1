\# Lil Buddy V1 System Architecture



This diagram shows how the main subsystems of Lil Buddy V1 connect together.





&nbsp;                   +---------------------------+

&nbsp;                   |   NVIDIA Jetson Orin Nano |

&nbsp;                   |   (AI Brain / Linux OS)   |

&nbsp;                   +------------+--------------+

&nbsp;                                |

&nbsp;                                | I2C

&nbsp;                                |

&nbsp;                     +----------v-----------+

&nbsp;                     |   PCA9685 Servo      |

&nbsp;                     |   Controller (PWM)   |

&nbsp;                     +----------+-----------+

&nbsp;                                |

&nbsp;              ----------------------------------------

&nbsp;              |             |             |          |

&nbsp;              v             v             v          v

&nbsp;       Shoulder Servo   Elbow Servo   Wrist Servo   Neck Servo

&nbsp;       (DS3218)         (DS3218)      (DS3218)      (DS3218)







---



&nbsp;               +-------------------------------+

&nbsp;               |       Power System            |

&nbsp;               |                               |

&nbsp;               |  4S LiPo Battery (14.8V)      |

&nbsp;               +---------------+---------------+

&nbsp;                               |

&nbsp;               ---------------------------------------

&nbsp;               |                                     |

&nbsp;               v                                     v



&nbsp;     +---------------------+           +----------------------+

&nbsp;     |  5V Buck Converter  |           |  6V Buck Converter   |

&nbsp;     |                     |           |                      |

&nbsp;     | Jetson Orin Nano   |           | Servo Power Rail     |

&nbsp;     | Cameras            |           | PCA9685 V+           |

&nbsp;     | Display            |           | Servo Motors         |

&nbsp;     +---------------------+           +----------------------+

---



&nbsp;            +-----------------------------+

&nbsp;            |        Vision System        |

&nbsp;            |                             |

&nbsp;            | Dual Cameras (Robot Eyes)  |

&nbsp;            | Computer Vision Models     |

&nbsp;            +--------------+--------------+

&nbsp;                           |

&nbsp;                           v



&nbsp;                   Object Detection

&nbsp;                   Face Recognition

&nbsp;                   Environment Awareness

---





&nbsp;            +-----------------------------+

&nbsp;            |         Voice System        |

&nbsp;            |                             |

&nbsp;            | Microphone                  |

&nbsp;            | Speech Recognition          |

&nbsp;            | Speaker Output              |

&nbsp;            +-----------------------------+

---





Subsystem Overview

AI Brain



Jetson Orin Nano runs:



Linux



Python robotics software



Computer vision models



Voice interaction system



Motion Control



Jetson communicates with the PCA9685 servo controller using the I2C bus.



The PCA9685 generates PWM signals for the robot's servos.



Servo Motors



High torque DS3218 servos control:



Shoulders



Elbows



Wrists



Neck



Power System



A 4S LiPo battery (14.8V) powers the robot.



Two buck converters create regulated voltage rails:



5V Rail



Jetson Orin Nano



Cameras



Display



6V Rail



PCA9685 servo rail



Servo motors



Vision System



Two cameras mounted in the robot head provide:



object detection



face recognition



environment awareness



Voice System



Microphone + speaker system allow:



speech recognition



voice responses







