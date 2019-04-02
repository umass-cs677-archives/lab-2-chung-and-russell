import csv
import requests
import time
import sys

SERVER_CONFIG = 'server_config'

#######################################################
############### Accessing Catalog server  #############
#######################################################


server_dict = {}
csv_reader = csv.DictReader(open(SERVER_CONFIG, mode ='r'))
for row in csv_reader:
    server_name = row['Server']
    server_dict[server_name] = {'Machine': row['Machine'],
                                'IP': row['IP'],
                                'Port': row['Port']}

FRONTEND_IP = server_dict['Frontend']['IP']
FRONTEND_PORT = server_dict['Frontend']['Port']
FRONTEND_ADDRESS = 'http://128.119.243.168:' + FRONTEND_PORT
print(FRONTEND_ADDRESS)

def search(topic, print_output = True):
    search_result = requests.get(FRONTEND_ADDRESS + '/search/' + topic).text
    if print_output:
        print(search_result)
    return search_result

def lookup(item_number, print_output = True):
    lookup_result = requests.get(FRONTEND_ADDRESS + '/lookup/' + str(item_number)).text
    if print_output:
        print(lookup_result)
    return lookup_result

def buy(catalog_id, print_output = True):
    buy_result = requests.get(FRONTEND_ADDRESS + '/buy/' + str(catalog_id)).text
    if print_output:
        print(buy_result)
    return buy_result

def sequential_query(query_fun, query_arg, iterations, write_file):
    with open(write_file,'w') as output_file:
        for i in range(iterations):
            start = time.time()
            query_result = query_fun(query_arg,print_output = False)
            runtime = time.time() - start
            output_file.write(str(runtime)+ '\n')



def main():
    command_fun_dict = {'buy':buy, 'search': search, 'lookup': lookup}
    call_string = sys.argv[1]
    call_function = command_fun_dict[call_string]
    call_argument = sys.argv[2]
    if len(sys.argv) > 3:
        iterations = int(sys.argv[3])
        filename = '../test/' + call_string + '_' + str(call_argument) + '_' + str(iterations) + '.txt'
        sequential_query(call_function,call_argument,iterations,filename)
        print ('Sequential ' + call_string + ' results written to ' + filename)
    else:
        call_function(call_argument)



if __name__ == '__main__':
    main()