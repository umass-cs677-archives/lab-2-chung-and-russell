#!/bin/bash
echo 10 clients, 1000 requests
wget -qO- http://128.119.243.164:5002/update/1/quantity/set/1100
curl http://128.119.243.147:5001/orders -X DELETE -v
python ../../src/Client.py buy 1 100 e3c1 -hide &
python ../../src/Client.py buy 1 100 e3c2 -hide &
python ../../src/Client.py buy 1 100 e3c3 -hide &
python ../../src/Client.py buy 1 100 e3c4 -hide &
python ../../src/Client.py buy 1 100 e3c5 -hide &
python ../../src/Client.py buy 1 100 e3c6 -hide &
python ../../src/Client.py buy 1 100 e3c7 -hide &
python ../../src/Client.py buy 1 100 e3c8 -hide &
python ../../src/Client.py buy 1 100 e3c9 -hide &
python ../../src/Client.py buy 1 100 e3c10 -hide

