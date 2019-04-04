# 677 Lab 2

The following distributed machine setup is REQUIRED:

    elnux1@cs.umass.edu/cs677/lab-2-chung-and-russell/src
    python Order.py
    
    elnux2@cs.umass.edu/cs677/lab-2-chung-and-russell/src
    python Catalog.py
    
    elnux3@cs.umass.edu/cs677/lab-2-chung-and-russell/src
    python Frontend.py
    
This can be done with the shellscript in ../src/server_startup.sh as described in its README.

run_tests.sh will run each of the following 4 tests, and save their outputs to test_outputs:

1. TestClientFunctions.sh: executes all 3 frontend operations from a single client with various scenarios, verify test by inspecting output.

2.  TestOrder.py: unit tests on order server.
3.  TestCatalogpy: unit tests on catalog server.
4.  test_concurrent.sh: spawns 5 clients to concurrently make buy requests, verify test by inspecting output.

All other shell scripts are performance experiments.
