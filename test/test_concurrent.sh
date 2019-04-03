#!/bin/bash
let INITIAL=3*$1
let EXPECTED=2*$1
echo Setting stock to $INITIAL_STOCK, 5 clients concurrently making $1 buys
wget -qO- http://128.119.243.164:5002/update/1/quantity/set/$INITIAL
python ../src/Client.py buy 1 $1 1conctest &
python ../src/Client.py buy 1 $1 2conctest &
python ../src/Client.py buy 1 $1 3conctest &
python ../src/Client.py buy 1 $1 4conctest &
python ../src/Client.py buy 1 $1 5conctest

wget -qO- http://128.119.243.164:5003
sleep 1
FAILED=$(grep -r 'conctest failed' | wc -l)
SUCCEEDED=$(grep -r 'conctest bought' | wc -l)

clear
echo $FAILED buys failed and $SUCCEEDED buys succeeded