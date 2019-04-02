# 677 Lab 2

The following distributed machine setup is REQUIRED:

    elnux1@cs.umass.edu/cs677/lab-2-chung-and-russell/src
    python Order.py
    
    elnux2@cs.umass.edu/cs677/lab-2-chung-and-russell/src
    python Catalog.py
    
    elnux3@cs.umass.edu/cs677/lab-2-chung-and-russell/src
    python Frontend.py
    
Running client processes on machine elnux7 is SUGGESTED:

    elnux7@cs.umass.edu/cs677/lab-2-chung-and-russell/src
    python Client.py [command] [command arg]
    
The following experiments can be executed as shell scripts from the test directory:

    elnux7@cs.umass.edu/cs677/lab-2-chung-and-russell/test
    chmod +x SequentialRequestExperiments.sh
    chmod +x TestClientFunctions.sh
    
    ./SequentialRequestExperiments.sh
    ./TestClientFunctions.sh
    
Can also save output of .sh files to txt:

    ./SequentialRequestExperiments.sh>seq_output.txt
    ./TestClientFunctions.sh>client_output.txt
    
