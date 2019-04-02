import csv
import requests
import time

FRONTEND_ADDRESS = 'http://128.119.243.168:5000'



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
            output_file.write(str(runtime) + ',' + query_result)


def main():
    help_string = "Available commands: \n  search <topic> \n  lookup <item number> \n  buy <item number> \n  quit\n"
    interactive_session = True
    while interactive_session:
        prompt = input("What do you want to do? \n").split()
        
        if prompt[0] == 'quit':
            interactive_session = False
        elif prompt[0] == 'help':
            print(help_string)
        elif prompt[0] == 'buy':
            try:
                item_number = str(prompt[1])
                if len(prompt) == 3:
                    iterations = str(prompt[2])
                    filename = 'buy_' + str(item_number) + '_' + str(iterations) + '.txt'
                    sequential_query(buy,item_number,iterations,filename)
                    print ('Sequential buy results written to ' + filename)
                else:
                    buy(item_number)
            except:
                "Error: bad input"
        elif prompt[0] == 'search':
            pass


if __name__ == '__main__':
    main()