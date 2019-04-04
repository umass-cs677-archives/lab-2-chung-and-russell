import unittest
import requests
import json


class TestCatalog(unittest.TestCase):

    def test_query_by_topic(self):

        response = requests.get("http://128.119.243.164:5002" + "/query/graduate_school")
        data = response.json()
        dic = {"items": {"Xen and the Art of Surviving Graduate School": 3, "Cooking for the Impatient Graduate Student":4}}
        self.assertDictEqual(data,dic)

        response = requests.get("http://128.119.243.164:5002" + "/query/distributed_systems")
        data = response.json()
        dic = {"items": {"How to get a good grade in 677 in 20 minutes a day": 1,
                         "RPCs for Dummies": 2}}

        self.assertDictEqual(data, dic)
        print("Querying message by topic correct dictionaries, passed")

    def test_query_by_item(self):

        response = requests.get("http://128.119.243.164:5002" + "/query/1")
        data = response.json()
        dict = list(data.values())[0]
        dict_keys = list(dict.keys())

        self.assertIn("COST", dict_keys)
        self.assertIn("QUANTITY", dict_keys)
        print("Query message by item correct keys, passed")

        self.assertIsInstance(dict["COST"], float)
        self.assertIsInstance(dict["QUANTITY"], int)
        print("Return types are correct")


    def test_update(self):
        response = requests.get("http://128.119.243.164:5002" + "/query/2")
        data = response.json()
        dict = list(data.values())[0]
        original_cost = dict["COST"]
        original_quantity = dict["QUANTITY"]

        # Make sure increase operation works correctly
        response = requests.get("http://128.119.243.164:5002" + "/update/2/cost/increase/5")
        data = response.json()
        dict = list(data.values())[0]
        updated_cost = dict["COST"]

        self.assertEqual(updated_cost - original_cost, 5)
        print("Increase operation correct amount, passed")

        # Make sure decrease operation works correctly
        response = requests.get("http://128.119.243.164:5002" + "/update/2/quantity/decrease/3")
        data = response.json()
        dict = list(data.values())[0]
        updated_quantity = dict["QUANTITY"]

        self.assertEqual(updated_quantity - original_quantity, -3)
        print("Decrease operation correct amount, passed")

        # Make sure set operation works correctly
        response = requests.get("http://128.119.243.164:5002" + "/update/2/quantity/set/120")
        data = response.json()
        dict = list(data.values())[0]
        updated_quantity = dict["QUANTITY"]

        self.assertEqual(updated_quantity, 120)
        print("Set operation correct amount, passed")





if __name__ == "__main__":
    unittest.main()