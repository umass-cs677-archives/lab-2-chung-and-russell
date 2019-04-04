#!/bin/bash

echo Setting stock to 300, 5 clients concurrently making 100 buys each
wget -qO- http://128.119.243.164:5002/update/1/quantity/set/300
python ../src/Client.py buy 1 100 1conctest &
python ../src/Client.py buy 1 100 2conctest &
python ../src/Client.py buy 1 100 3conctest &
python ../src/Client.py buy 1 100 4conctest &
python ../src/Client.py buy 1 100 5conctest

wget -qO- http://128.119.243.164:5003
sleep 1
FAILED_COUNT=$(grep -r 'conctest failed' | wc -l)
SUCCEEDED_COUNT=$(grep -r 'conctest bought' | wc -l)

let FAILED=$FAILED_COUNT-1
let SUCCEEDED=$SUCCEEDED_COUNT-1


echo $FAILED buys failed and $SUCCEEDED buys succeeded
wget -qO- http://128.119.243.168:5003/lookup/1