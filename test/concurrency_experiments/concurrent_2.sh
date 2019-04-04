#!/bin/bash
echo 2 clients, 100 requests
wget -qO- http://128.119.243.164:5002/update/1/quantity/set/1500
curl http://128.119.243.147:5001/orders -X DELETE -v
python ../../src/Client.py buy 1 100 e1c1 -hide &
python ../../src/Client.py buy 1 100 e1c2 -hide


