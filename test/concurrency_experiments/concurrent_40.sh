#!/bin/bash
echo 40 clients, 100 requests
wget -qO- http://128.119.243.164:10002/update/1/quantity/set/4400
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
python ../../src/Client.py buy 1 100 e4c20 -hide &
python ../../src/Client.py buy 1 100 e4c21 -hide &
python ../../src/Client.py buy 1 100 e4c22 -hide &
python ../../src/Client.py buy 1 100 e4c23 -hide &
python ../../src/Client.py buy 1 100 e4c24 -hide &
python ../../src/Client.py buy 1 100 e4c25 -hide &
python ../../src/Client.py buy 1 100 e4c26 -hide &
python ../../src/Client.py buy 1 100 e4c27 -hide &
python ../../src/Client.py buy 1 100 e4c28 -hide &
python ../../src/Client.py buy 1 100 e4c29 -hide &
python ../../src/Client.py buy 1 100 e4c30 -hide &
python ../../src/Client.py buy 1 100 e4c31 -hide &
python ../../src/Client.py buy 1 100 e4c32 -hide &
python ../../src/Client.py buy 1 100 e4c33 -hide &
python ../../src/Client.py buy 1 100 e4c34 -hide &
python ../../src/Client.py buy 1 100 e4c35 -hide &
python ../../src/Client.py buy 1 100 e4c36 -hide &
python ../../src/Client.py buy 1 100 e4c37 -hide &
python ../../src/Client.py buy 1 100 e4c38 -hide &
python ../../src/Client.py buy 1 100 e4c39 -hide &
python ../../src/Client.py buy 1 100 e4c40 -hide

