#!/bin/bash
curl http://128.119.243.147:5001/orders -X DELETE -v
echo Setting stocks to varying quantity and making 10 buys
wget -qO- http://128.119.243.164:5002/update/1/quantity/set/1500
wget -qO- http://128.119.243.164:5002/update/2/quantity/set/1200
wget -qO- http://128.119.243.164:5002/update/3/quantity/set/1000
wget -qO- http://128.119.243.164:5002/update/4/quantity/set/500
python ../src/Client.py buy 1 1000 c1 -hide
python ../src/Client.py buy 2 1000 c1 -hide
python ../src/Client.py buy 3 1000 c1 -hide
python ../src/Client.py buy 4 1000 c1 -hide

curl http://128.119.243.147:5001/orders -X DELETE -v
echo Looking up resulting stock, should be 500,200,0,0
python ../src/Client.py lookup 1 1000 c1 -hide 
python ../src/Client.py lookup 2 1000 c1 -hide 
python ../src/Client.py lookup 3 1000 c1 -hide 
python ../src/Client.py lookup 4 1000 c1 -hide

curl http://128.119.243.147:5001/orders -X DELETE -v
echo Doing lookup 10 times
python ../src/Client.py lookup 1 1000 c1 -hide
python ../src/Client.py lookup 2 1000 c1 -hide
python ../src/Client.py lookup 3 1000 c1 -hide
python ../src/Client.py lookup 4 1000 c1 -hide

curl http://128.119.243.147:5001/orders -X DELETE -v
echo Doing topic search lookup 1000 times
python ../src/Client.py search graduate_school 1000 c1 -hide
python ../src/Client.py search distributed_systems 1000 c1 -hide



