#!/bin/bash

echo Reset stock and order database
wget -qO- http://128.119.243.164:5002/update/1/quantity/set/0
curl http://128.119.243.147:5001/orders -X DELETE -v
python ../src/Client.py buy 1 1000 tierClient
wget -qO- http://128.119.243.147:5001/orders>orders.txt
cat orders.txt | sed -n 1'p' | tr ',' '\n' | grep '^"p' | grep -Eo "[0-9]+\.[0-9]+" > buy_query_times.txt





