from unittest import TestCase
from fake_useragent import UserAgent
import requests as r
import random
import time
class KafkaTestClass():
    ua = UserAgent()
    ua.random
    s = r.Session()
    add_url = 'http://127.0.0.1:8000/addToBasket/'
    order_url = 'http://127.0.0.1:8000/order/'
    def load_test(self):
        while True:
            self.s.post(url  = self.add_url,data = {
                "product_id": random.randint(1,3),
                "quantity": random.randint(1,111)
            })
            res = self.s.post(url = self.order_url,
            data = {
                "email": 'op1um@xyu.com',
                "username": 'op1um'
            })

test = KafkaTestClass()
test.load_test()