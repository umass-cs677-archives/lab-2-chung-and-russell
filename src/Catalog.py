import re
from flask import Flask, request, jsonify

app = Flask("catalog")

def _load_books(db_name):
    """
    This function takes the database name and convert the content to a dictionary

    :param db_name: data base name
    :return: dictionary with ID as key and a tuple that stores information of a book as value
    """

    book_info = {}

    with open(db_name) as f:
        lines = f.readlines()

        #First line is column names so we toss it
        for line in lines[1:]:
            col = re.split(",\s*", line.replace("\n",""))
            book_info[int(col[0])] = tuple(col[i] for i in range(1,len(col)))

    return book_info

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

    return query_result

@app.route("/update/<field>/<operation>/<int:number>", methods=['PUT'])
def update(field, operation, number):
    """

    Update field using given operation and number

    :param name: name of the field to update
    :param operation: three operations are supported. increase, decrease, and set
    :param number: number to be used in operation
    :return: status code
    """



    print("hi")



if __name__ == "__main__":

    app.run(use_debugger = False, use_reloader = False, debug = True)

