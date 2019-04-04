#!/bin/bash
echo 5 clients, 100 requests
wget -qO- http://128.119.243.164:5002/update/1/quantity/set/4000
curl http://128.119.243.147:5001/orders -X DELETE -v
python ../../src/Client.py buy 1 100 e2c1 -hide &
python ../../src/Client.py buy 1 100 e2c2 -hide &
python ../../src/Client.py buy 1 100 e2c3 -hide &
python ../../src/Client.py buy 1 100 e2c4 -hide &
python ../../src/Client.py buy 1 100 e2c5 -hide

