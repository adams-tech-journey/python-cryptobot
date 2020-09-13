import time

from crypto_values import GetNowPrice, BoughtPrice, Total_Shares
from send_mail import SendMail


p1 = GetNowPrice()
b1 = BoughtPrice(2.5)
t1 = Total_Shares(25)
s1 = SendMail()


current_value = (p1.get_price()*t1.NoShares())
current_value_round = round(current_value,3)
past_value = ((b1.bought_price()* t1.NoShares()))
profit_percentage = ((current_value/past_value) * 100)


if current_value > (past_value * 0.05):
        s1.send_slack( "\n Original Portfolio: £" + str(past_value) + "\n Price Portfolio now: £" + str(current_value_round) + "\n Profit Percentage: " + str(profit_percentage)+"%")
                # print("\n Original Portfolio: £" + str(past_value) + "\n Price Portfolio now: £" + str(current_value_round) + "\n Profit Percentage: " + str(profit_percentage)+"%")
     



