from flask import Flask
import requests

app = Flask("frontend")



@app.route("/search/<topic>", methods = ["GET"])
def search(topic):
    books = requests.get("http://128.119.243.164:5000/query/" + topic).json()

    search_result = []

    for book in books["items"]:
        search_result.append("Name: ")
        search_result.append(book)
        search_result.append(" Item ID: ")
        search_result.append(str(books["items"][book]))
        search_result.append("\n")

    return("".join(search_result))


@app.route("/lookup/<item_number>")
def lookup(item_number):
    books = requests.get("http://128.119.243.164:5000/query/" + item_number).json()

    search_result = []

    for book in books:
        search_result.append("Name: ")
        search_result.append(book)
        search_result.append("\n")
        search_result.append("Cost: ")
        search_result.append(str(books[book]["COST"]))
        search_result.append("\n")
        search_result.append("Quantity: ")
        search_result.append(str(books[book]["QUANTITY"]))
        search_result.append("\n")


    return "".join(search_result)

@app.route("/buy/<catalog_id>")
def buy(catalog_id):
    response = requests.get("http://128.119.243.147:5000/buy/" + catalog_id).json()

    if response["is_successful"]:
        return "bough book "
    return("")

if __name__ == "__main__":

    app.run(debug=True,host='0.0.0.0')
