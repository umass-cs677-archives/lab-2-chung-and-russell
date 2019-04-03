#!/bin/bash
echo Setting stock to 1500
wget -qO- http://128.119.243.164:5002/update/1/quantity/set/1500
python ../src/Client.py buy 1 100 e1c1 &
python ../src/Client.py buy 1 100 e1c2

