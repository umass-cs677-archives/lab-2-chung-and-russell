import unittest
import urllib.request
import json

class TestCatalog(unittest.TestCase):


    def test_query_by_topic(self):

        response = urllib.request.urlopen("http://127.0.0.1:5000/query/graduateschool")
        data = json.load(response)
        dic = {"items": {"Xen and the Art of Surviving Graduate School": 3, "Cooking for the Impatient Graduate Student":4}}
        self.assertDictEqual(data,dic)

        response = urllib.request.urlopen("http://127.0.0.1:5000/query/distributedsystems")
        data = json.load(response)
        dic = {"items": {"How to get a good grade in 677 in 20 minutes a day": 1,
                         "RPCs for Dummies": 2}}
        self.assertDictEqual(data, dic)


    def test_query_by_item(self):

        response = urllib.request.urlopen("http://127.0.0.1:5000/query/1")
        data = json.load(response)
        dict = list(data.values())[0]
        dict_keys = list(dict.keys())

        self.assertIn("cost", dict_keys)
        self.assertIn("number in stock", dict_keys)

        self.assertIsInstance(dict["cost"], int)
        self.assertIsInstance(dict["number in stock"], int)


if __name__ == "__main__":
    unittest.main()