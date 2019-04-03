#!/bin/bash
echo Setting stock to 6000
wget -qO- http://128.119.243.164:5002/update/1/quantity/set/4000
python ../src/Client.py buy 1 1000 e2c1 &
python ../src/Client.py buy 1 1000 e2c2 &
python ../src/Client.py buy 1 1000 e2c3 &
python ../src/Client.py buy 1 1000 e2c4 &
python ../src/Client.py buy 1 1000 e2c5
echo Lookup ending stock
wget -qO- http://128.119.243.168:5003/lookup/1

