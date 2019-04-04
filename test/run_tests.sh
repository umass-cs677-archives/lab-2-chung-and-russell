#!/bin/bash
echo 'Running TestClientFunctions.sh'
./TestClientFunctions.sh>test_outputs/TestClientFunctions.txt
echo 'Output saved to test_outputs/'
echo 'Running TestOrder.py'
python3 TestOrder.py>test_outputs/TestOrder_output.txt
echo 'Output saved to test_outputs/'
echo 'Running TestCatalog.py'
python3 TestCatalog.py>test_outputs/TestCatalog_output.txt
echo 'Output saved to test_outputs/'
echo 'Running test_concurrent.sh'
./test_concurrent.sh>test_outputs/test_concurrent_output.txt
echo 'Output saved to test_outputs/'

