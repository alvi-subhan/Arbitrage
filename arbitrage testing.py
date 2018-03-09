import urllib.parse, requests,json
from matplotlib import pyplot as plt
import numpy as np

main_url="https://api.cryptonator.com/api/full/"
add="btc-usd"

url=main_url+add
print(url)
json_data=requests.get(url).json()

#this is the output from the json_data
"""{
  "ticker": {
    "base": "BTC",
    "target": "USD",
    "price": "8850.69012695",
    "volume": "168611.95114534",
    "change": "3.57147475",
    "markets": []
  }
}"""

crypto_currency=json_data["ticker"]["markets"]

price_float=[]
market_names=[]

for mt in crypto_currency:
     #print(mt["market"])

     xy=float(mt["price"])
     price_float.append(xy)
     yx=mt["market"]
     market_names.append(yx)

#print(price_float)
#print(market_names)

price_float=np.array(price_float)

index_min_price=np.argmin(price_float)
index_max_price=np.argmax(price_float)

min_price=np.take(price_float,index_min_price)
max_price=np.take(price_float,index_max_price)

min_market=np.take(market_names,index_min_price)
max_market=np.take(market_names,index_max_price)

round_min=round(min_price,4)
round_max=round(max_price,4)

profit=round_max-round_min

profit_percent=np.round( ((max_price-min_price)/min_price)*100 ,3) #roumded the profit

print("Buy from ",min_market,"at price ",str(round_min)," and sell it in ",max_market," for ",str(round_max))
print("\nYou can make a profit of ",str(profit)," which is" ,str(profit_percent),"%")

