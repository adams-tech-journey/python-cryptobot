import json

import requests


class GetNowPrice:
    def __init__(self):
     self.url = 'https://min-api.cryptocompare.com/data/price?fsym=LINK&tsyms=GBP'

    def get_price(self):
        response = requests.get(self.url)
        data = response.json()
        price = float(data["GBP"])
        return price
        if response.status_code == 200:
            return json.loads(response.content.decode('utf-8'))
        else:
            return None

class BoughtPrice:
    def __init__(self, bought_price):
        self.boughtPrice = bought_price

    def bought_price(self):
        return self.boughtPrice

class Total_Shares():
    def __init__(self, shares):
        self.shares = shares
    def NoShares(self):
        return self.shares

#
# class Adams_current_portfolio(BoughtPrice):
#
#     def __init__(self, price, shares):
#         self.price = price
#         self.shares = shares
#         self.bought_price().boughtPrice
#
#
#     def total_value (self):
#         return (self.price * self.shares)
#
#     def current_value(self):
#         return GetNowPrice().get_price()*Total_Shares.NoShares()
#
#     def past_value(self):
#      BoughtPrice.bought_price(self.boughtprice)* Total_Shares.NoShares()
#
#
