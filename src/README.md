# 677 Lab 2

How to call client from command line:

python Client.py [operation] [operation argument] [number of sequential requests (OPTIONAL)]
List of operations and their corresponding arguments:
  1. buy
    argument: item_ID
    argument values: 1,2,3,4
  2. lookup
    argument: item_ID
    argument values: 1,2,3,4
  3. search
    argument: topic
    arguments: graduate_school, distributed_systems
    
Examples:
  python Client.py buy 1
  python Client.py buy 1 1000
  python Client.py search graduate_school
  python Client.py lookup 3 50
    
Omitting the number of sequential requests will cause the client to call the frontend once, and print out the result.
Including the number of sequential requests will ignore frontend results, and simply record the end-to-end response times in a .txt file.
