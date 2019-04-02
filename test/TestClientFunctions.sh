#!/bin/bash

echo Buying first item 5 times, starting at stock 6
wget -qO- http://128.119.243.164:5002/update/1/quantity/set/6
python ../src/Client.py buy 1
python ../src/Client.py buy 1
python ../src/Client.py buy 1
python ../src/Client.py buy 1
python ../src/Client.py buy 1
echo Looking up final stock of first item
python ../src/Client.py lookup 1 

echo Buying second item 5 times, starting at stock 5
wget -qO- http://128.119.243.164:5002/update/2/quantity/set/5
python ../src/Client.py buy 2 
python ../src/Client.py buy 2 
python ../src/Client.py buy 2 
python ../src/Client.py buy 2 
python ../src/Client.py buy 2 
echo Looking up final stock of second item
python ../src/Client.py lookup 2 

echo Buying third item 5 times, starting at stock 4
wget -qO- http://128.119.243.164:5002/update/3/quantity/set/4
python ../src/Client.py buy 3 
python ../src/Client.py buy 3 
python ../src/Client.py buy 3 
python ../src/Client.py buy 3 
python ../src/Client.py buy 3 
echo Looking up final stock of third item
python ../src/Client.py lookup 3 

echo Buying fourth item 5 times, starting at stock 3
wget -qO- http://128.119.243.164:5002/update/4/quantity/set/3
python ../src/Client.py buy 4 
python ../src/Client.py buy 4 
python ../src/Client.py buy 4 
python ../src/Client.py buy 4 
python ../src/Client.py buy 4 
echo Looking up final stock of fourth item
python ../src/Client.py lookup 4 

echo Searching topic 'graduate_school'
python ../src/Client.py search graduate_school
echo Searching topic 'distributed_systems'
python ../src/Client.py search distributed_systems 
echo Done testing basic client operations!



