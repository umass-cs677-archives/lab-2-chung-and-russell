#!/bin/bash
echo 20 clients, 100 requests
wget -qO- http://128.119.243.164:5002/update/1/quantity/set/1500
curl http://128.119.243.147:5001/orders -X DELETE -v
python ../../src/Client.py buy 1 100 e4c1 -hide &
python ../../src/Client.py buy 1 100 e4c2 -hide &
python ../../src/Client.py buy 1 100 e4c3 -hide &
python ../../src/Client.py buy 1 100 e4c4 -hide &
python ../../src/Client.py buy 1 100 e4c5 -hide &
python ../../src/Client.py buy 1 100 e4c6 -hide &
python ../../src/Client.py buy 1 100 e4c7 -hide &
python ../../src/Client.py buy 1 100 e4c8 -hide &
python ../../src/Client.py buy 1 100 e4c9 -hide &
python ../../src/Client.py buy 1 100 e4c10 -hide &
python ../../src/Client.py buy 1 100 e4c11 -hide &
python ../../src/Client.py buy 1 100 e4c12 -hide &
python ../../src/Client.py buy 1 100 e4c13 -hide &
python ../../src/Client.py buy 1 100 e4c14 -hide &
python ../../src/Client.py buy 1 100 e4c15 -hide &
python ../../src/Client.py buy 1 100 e4c16 -hide &
python ../../src/Client.py buy 1 100 e4c17 -hide &
python ../../src/Client.py buy 1 100 e4c18 -hide &
python ../../src/Client.py buy 1 100 e4c19 -hide &
python ../../src/Client.py buy 1 100 e4c20 -hide

