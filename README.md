Publish csv data to html datatable
=================================================

Requirements
--------------------------

- python3
- virtualenv


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

- visit: http://localhost:5000/
