# Plane Localizarion

## Overview

The goal is to localize a flying plane in three dimensional space. For this the following hadrware is used.  
* Raspberry Pi 3B  
* [Sparkfun 9DoF Razor IMU M0](https://learn.sparkfun.com/tutorials/9dof-razor-imu-m0-hookup-guide)  
* [GYNEO6 V2 GPS Module](https://www.amazon.com/GY-GPS6MV2-NEO6MV2-Antenna-Arduino-Control/dp/B07QMTM5YM)    

## Setting up IMU
Sparkfun Razor IMU M0 comes with USB port which makes it easy to interface. The default firmware whcih comes with it is not compatible with ROS so this has to be updated to make it fully compatible with ROS. The firmware can be updated by follwing the steps [here](https://learn.sparkfun.com/tutorials/9dof-razor-imu-m0-hookup-guide) and using [this](https://github.com/lebarsfa/razor-9dof-ahrs) firmware. 

## Testing
### GPS
To test the GPS, make sure the GPS is connected to the serial port and that port is prelividged to read and execute. After going the ROS workspace, run the commands below to test the GPS.

```
roscore # If it's not already running
cd ~/catkin_ws # Your path may vary
source devel/setup.bash
sudo chmod 666 /dev/ttyUSB0
rosrun nmea_navsat_driver nmea_serial_driver _port:=/dev/ttyUSB0 _baud:=9600

```

### GPS Logging
To log GPS, there is a separate ROS node `gps_log.py` in the package `data_log`. Follow the instruction below to log the GPS in `.csv` file. This file is placed in the base directory i.e. `plane_localization` and automatically named `gps current data + time.csv`.

 ```
 sudo chmod +x src/data_log/gps_log.py 
 rosrun data_log gps_log.py
 ```
