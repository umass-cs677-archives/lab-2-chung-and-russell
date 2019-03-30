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
            book_info[col[0]] = tuple(col[i] for i in range(1,len(col)))

    return book_info

def _filter_by_topic(book_info, topic):
    """
    Return names and IDs of books with specified topic

    :param book_info: list of tuples that contain information of books
    :param topic: a string that specified the topic of interest
    :return: dictionary that maps bookname to its id
    """
    sorted_books = {}
    topic = topic.lower()

    for book_id , info in book_info.items():
        book_topic = info[0].lower().replace(" ", "")
        book_name = info[1]
        
        if book_topic == topic:
            sorted_books[book_name] = book_id

    return sorted_books

# def _filter_by_item(book_info, item_id):
#     """
#      Return cost and number of items in stocks for a book with item_id
#
#     :param book_info: list of tuples that contain information of books
#     :param item_id: unique id for the book
#     :return: dictionary that stores the cost and number of items in stock for a book with item_id
#     """
#
#     for book in book_info:
#

@app.route("/query/<topic>", methods=['GET'])
@app.route("/query/<int:item_number>", methods=['GET'])
def query(**kwargs):

    key = list(kwargs)[0]
    book_info = _load_books("inventory")

    if key == "topic":
        filtered_book = _filter_by_topic(book_info, kwargs[key])
        search_result = jsonify(items = filtered_book)
        return search_result

    elif key == "item_number":
        return "hey"

@app.route("/lookup", methods=['GET'])
def update():
    print("")


if __name__ == "__main__":

    app.run(use_debugger = False, use_reloader = False, debug = True)

