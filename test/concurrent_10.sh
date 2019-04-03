#!/bin/bash
echo Setting stock to 6000
wget -qO- http://128.119.243.164:5002/update/1/quantity/set/1100
python ../src/Client.py buy 1 100 e3c1 &
python ../src/Client.py buy 1 100 e3c2 &
python ../src/Client.py buy 1 100 e3c3 &
python ../src/Client.py buy 1 100 e3c4 &
python ../src/Client.py buy 1 100 e3c5 &
python ../src/Client.py buy 1 100 e3c6 &
python ../src/Client.py buy 1 100 e3c7 &
python ../src/Client.py buy 1 100 e3c8 &
python ../src/Client.py buy 1 100 e3c9 &
python ../src/Client.py buy 1 100 e3c10

