from flask import Flask
from flask import jsonify
from flask_restful import reqparse, abort, Api, Resource
import csv
import random
import time

app = Flask(__name__)
api = Api(app)

ORDER_FILE = 'order_log.txt'

#######################################################
#### Helper functions for read/writing to order DB ####
#######################################################
def reset_orders():
    # initialize order database as a local .txt file
    with open(ORDER_FILE, mode='w') as order_log:
        fieldnames = ['order_id', 'processing_time','is_successful','catalog_id']
        writer = csv.DictWriter(order_log, fieldnames=fieldnames)

        writer.writeheader()
        # TODO: has some dummy orders for now.  for submission, order log should be empty
        writer.writerow({'order_id': 1, 'processing_time': .123, 'is_successful': True, 'catalog_id': 345})
        writer.writerow({'order_id': 2, 'processing_time': .023, 'is_successful': False,'catalog_id': 359})
        writer.writerow({'order_id': 3, 'processing_time': .023, 'is_successful': False,'catalog_id': 359})
        order_log.close()


def get_orders_as_dict():
    #orders = {}
    with open(ORDER_FILE, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        return [row for row in csv_reader]
        #for row in csv_reader:
        #    orders[row["order_id"]] = {"processing_time": row["processing_time"],
        #                                "is_successful": row["is_successful"],
        #                                "catalog_id": row["catalog_id"]}
    #return orders

def get_num_orders():
    orders = get_orders_as_dict()
    return len(orders)

def create_order(order_id,processing_time,is_successful,catalog_id):
    return {'order_id': order_id,
            'processing_time': processing_time,
            'is_successful': is_successful,
            'catalog_id': catalog_id}

def write_order(order):
    with open(ORDER_FILE, mode='a') as order_log:
        fieldnames = ['order_id', 'processing_time','is_successful','catalog_id']
        writer = csv.DictWriter(order_log, fieldnames=fieldnames)
        print(type(order))
        writer.writerow(order)

#######################################################
######## Functions for querying catalog server ########
#######################################################

parser = reqparse.RequestParser()
parser.add_argument('catalog_id', type = int, help = 'Catalog ID for item to buy')

#TODO: integrate with catalog server API
# until then, just wait a random amount of time
def query_catalog_server(catalog_id):
    timeDelay = random.randrange(0, 2)
    time.sleep(timeDelay)
    return random.randint(0,4)

def decrement_catalog_server(catalog_id):
    timeDelay = random.randrange(0, 2)
    time.sleep(timeDelay)


######################################################
################ Setup REST resources ################
######################################################

# Buy
# submit a single buy request

class Buy(Resource):
    order = {}
    def get(self, catalog_id):
        start = time.time()
        stock = query_catalog_server(catalog_id)
        processing_time = time.time() - start
        if stock == 0:
            # done querying the catalog server, add an order to the order DB
            order_id = get_num_orders() + 1
            is_successful = False
            
        else:
            #decrement stock by 1
            decrement_catalog_server(catalog_id)
            is_successful = True
            order_id = get_num_orders() + 1
        
        order = create_order(order_id,processing_time,is_successful,catalog_id)
        write_order(order)
        return(order)


# OrderList
# shows a list of all orders
class OrderList(Resource):
    def get(self):
        orders = get_orders_as_dict()
        return jsonify(orders)
    
    def reset(self):
        reset_orders()
        orders = get_orders_as_dict()
        return jsonify(orders)

##
## setup the Api resource routing here
##
api.add_resource(OrderList, '/orders')
api.add_resource(Buy, '/orders/<catalog_id>')



# TODO setup public flask server
if __name__ == '__main__':
    app.run( debug=True)
