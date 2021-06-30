Publish csv data to html datatable
=================================================

Requirements
--------------------------

- python3
- Raspberry pi 4
- MPU6000 accelerometer and inclinometer


Installation
--------------------------

``` bash
# install virtualenv
sudo apt install python3-virtualenv
# Create virtualenv
python3 -m virtualenv -p python3 .venv
# Activate virtualenv
source .venv/bin/activate
# Install the requirements
pip3 install -r requirements.txt
#install the requirements 
sudo pip3 install adafruit-circuitpython-mpu6050
```

Run
--------------------------

``` bash
# Activate virtualenv
source .venv/bin/activate
# Start the web server
python tabla_sensor_rasp.py
```

Problems solve
--------------------------
If theres an error in virtual enviroment install were the path isnot fount run the next code:
export PATH=/home/pi/.local/bin:$PAT
this code import the path for the virtual enviroment 
