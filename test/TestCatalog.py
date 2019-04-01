import unittest
import urllib.request
import json
class TestCatalog(unittest.TestCase):

    def test_query_by_topic(self):

        response = urllib.request.urlopen("http://0.0.0.0:5000/query/graduate_school")
        data = json.load(response)
        dic = {"items": {"Xen and the Art of Surviving Graduate School": 3, "Cooking for the Impatient Graduate Student":4}}
        self.assertDictEqual(data,dic)

        response = urllib.request.urlopen("http://0.0.0.0:5000/query/distributed_systems")
        data = json.load(response)
        dic = {"items": {"How to get a good grade in 677 in 20 minutes a day": 1,
                         "RPCs for Dummies": 2}}
        self.assertDictEqual(data, dic)


    def test_query_by_item(self):

        response = urllib.request.urlopen("http://0.0.0.0:5000/query/1")
        data = json.load(response)
        dict = list(data.values())[0]
        dict_keys = list(dict.keys())

        self.assertIn("COST", dict_keys)
        self.assertIn("QUANTITY", dict_keys)

        self.assertIsInstance(dict["COST"], float)
        self.assertIsInstance(dict["QUANTITY"], int)


    def test_update(self):
        response = urllib.request.urlopen("http://0.0.0.0:5000/query/2")
        data = json.load(response)
        dict = list(data.values())[0]
        original_cost = dict["COST"]
        original_quantity = dict["QUANTITY"]

        # Make sure increase operation works correctly
        response = urllib.request.urlopen("http://0.0.0.0:5000/update/2/cost/increase/5")
        data = json.load(response)
        dict = list(data.values())[0]
        updated_cost = dict["COST"]

        self.assertEqual(updated_cost - original_cost, 5)

        # Make sure decrease operation works correctly
        response = urllib.request.urlopen("http://0.0.0.0:5000/update/2/quantity/decrease/3")
        data = json.load(response)
        dict = list(data.values())[0]
        updated_quantity = dict["QUANTITY"]

        self.assertEqual(updated_quantity - original_quantity, -3)

        # Make sure set operation works correctly
        response = urllib.request.urlopen("http://0.0.0.0:5000/update/2/quantity/set/120")
        data = json.load(response)
        dict = list(data.values())[0]
        updated_quantity = dict["QUANTITY"]

        self.assertEqual(updated_quantity, 120)





if __name__ == "__main__":
    unittest.main()