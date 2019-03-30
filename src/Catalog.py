import re
from flask import Flask, request, jsonify

app = Flask("catalog")

def _load_books(db_name):
    """
    This function takes the database name and load the content into a list of tuples.
    Database here is just a text file.

    :param db_name: data base name
    :return: column names, information about all books in the database
    """

    book_info = []

    with open(db_name) as f:
        lines = f.readlines()

        #First line is column names so we toss it
        for line in lines[1:]:
            col = re.split(",\s*", line.replace("\n",""))
            book_info.append(tuple(col[i] for i in range(len(col))))

    return book_info

def _filter_by_topic(book_info, topic):
    """
    Return books with specified topic

    :param book_info: list of tuples that contain information of books
    :param topic: a string that specified the topic of interest
    :return: dictionary and books' names and quantities
    """
    sorted_books = {}
    topic = topic.lower()

    for book in book_info:
        book_topic = book[1].lower().replace(" ", "")
        book_name = book[2]
        book_quantity = int(book[3])

        if book_topic == topic:
            sorted_books[book_name] = book_quantity

    return sorted_books


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

