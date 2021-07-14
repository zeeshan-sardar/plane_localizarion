# Plane Localizarion

## Overview

The goal is to localize a flying plane in three dimensional space. For this the following hadrware is used.  
* Raspberry Pi 3B  
* [Sparkfun 9DoF Razor IMU M0](https://learn.sparkfun.com/tutorials/9dof-razor-imu-m0-hookup-guide)  
*[GYNEO6 V2 GPS Module](https://www.amazon.com/GY-GPS6MV2-NEO6MV2-Antenna-Arduino-Control/dp/B07QMTM5YM)    

## Setting up IMU
Sparkfun Razor IMU M0 comes with USB port which makes it easy to interface. The default firmware whcih comes with it is not compatible with ROS so this has to be updated to make it fully compatible with ROS. The firmware can be updated by follwing the steps [here](https://learn.sparkfun.com/tutorials/9dof-razor-imu-m0-hookup-guide) and using [this](https://github.com/lebarsfa/razor-9dof-ahrs) firmware. 

