import re
import sqlite3
from flask import Flask, request, jsonify, abort, g

app = Flask("catalog")
DATABASE = 'inventory.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()



def _filter_by_topic(book_info, topic):
    """
    Return names and IDs of books with specified topic

    :param book_info: list of tuples that contain information of books
    :param topic: a string that specified the topic of interest
    :return: dictionary that maps bookname to its id
    """
    filtered_books = {}
    topic = topic.lower()

    for book_id , info in book_info.items():
        book_topic = info[0].lower().replace(" ", "")
        book_name = info[1]

        if book_topic == topic:
            filtered_books[book_name] = book_id

    return filtered_books

def _filter_by_item(book_info, item_id):
    """
     Return cost and number of items in stocks for a book with item_id

    :param book_info: dictionary that stores information of all items
    :param item_id: unique id for the book
    :return: dictionary that stores the cost and number of items in stock for a book with item_id
    """

    item_info = {"cost" : int(book_info[item_id][3]), "number in stock": int(book_info[item_id][2])}

    return item_info


@app.route("/query/<topic>", methods=['GET'])
@app.route("/query/<int:item_number>", methods=['GET'])
def query(**kwargs):

    key = list(kwargs)[0]
    book_info = _load_books("inventory")

    if key == "topic":
        filter_result = _filter_by_topic(book_info, kwargs[key])
        query_result = jsonify(items=filter_result)

    elif key == "item_number":
        filter_result = _filter_by_item(book_info, kwargs[key])
        book_name = book_info[kwargs[key]][1]
        query_result = jsonify({book_name: filter_result})

    else:
        return "no query criteria specified"

    return query_result

@app.route("/update/<item_id>/<field>/<operation>/<int:number>", methods=['PUT'])
def update(item_id, field, operation, number = 1):
    """

    Update field using given operation and number

    :param name: name of the field to update
    :param operation: three operations are supported. increase, decrease, and set
    :param number: number to be used in operation
    :return: status code
    """
    book_info = _filter_by_item(_load_books("inventory"), item_id)

    valid_fields = ["cost", "quantity"]
    valid_operation = ["increase", "decrease", "set"]

    if field not in valid_fields:
        abort(400)

    if operation not in valid_operation:
        abort(400)




if __name__ == "__main__":
    app.run(use_debugger = False, use_reloader = False, debug = True)

