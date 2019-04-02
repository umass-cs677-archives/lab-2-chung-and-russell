import unittest
import urllib.request
import requests
import json




class TestOrder(unittest.TestCase):

    def test_buy_item_title(self):
        titles = ["How to get a good grade in 677 in 20 minutes a day",
                  "RPCs for Dummies",
                  "Xen and the Art of Surviving Graduate School",
                  "Cooking for the Impatient Graduate Student"]
        
        responses = [json.load(urllib.request.urlopen("http://128.119.243.147:5001/buy/" + item_id))
                    for item_id in ['1','2','3','4']]
        
        response_titles = [response['title'] for response in responses]

        for (title,response_title) in zip(titles,response_titles):
            self.assertMultiLineEqual(title,response_title)

        print("Buy fetches correct title, passed")

    def test_return_types(self):

        data = json.load(urllib.request.urlopen("http://128.119.243.147:5001/buy/1"))
        dict_keys = list(data.keys())

        self.assertIn("catalog_id", dict_keys)
        self.assertIn("is_successful", dict_keys)
        self.assertIn("order_id", dict_keys)
        self.assertIn("processing_time", dict_keys)
        self.assertIn("title", dict_keys)
        print("Buy return fields, passed")

        self.assertIsInstance(data["catalog_id"], str)
        self.assertIsInstance(data["is_successful"], bool)
        self.assertIsInstance(data["order_id"], int)
        self.assertIsInstance(data["processing_time"], float)
        self.assertIsInstance(data["title"], str)
        print("Return types are correct")


    def test_buy_success(self):
        # set stock to 1
        requests.get("http://128.119.243.164:5002/update/1/quantity/set/1")

        data1 = json.load(urllib.request.urlopen("http://128.119.243.147:5001/buy/1"))
        first_buy = data1['is_successful']
        self.assertTrue(first_buy)

        print("Successful buy passed")

        # stock is now 0, next buy should fail
        data2 = json.load(urllib.request.urlopen("http://128.119.243.147:5001/buy/1"))
        second_buy = data2['is_successful']
        self.assertFalse(second_buy)
        print("Unsuccessful buy passed")





if __name__ == "__main__":
    unittest.main()