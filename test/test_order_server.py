import requests



def initial_tests():
    response = requests.get('http://127.0.0.1:5000/orders')
    print(response.json())


if __name__ == '__main__':
    initial_tests()