

# app/robo_advisor.py


import csv
import json
import os


import requests


import datetime


def to_usd (my_price):
   return "${0:,.2f}".format(my_price)
#
#Info inputs
#

request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=5min&apikey=demo"
response = requests.get(request_url) 
#print(type(response))#<class 'requests.models.Response'>
#print(response.status_code)#>200
#print(response.text)#

parsed_response = json.loads(response.text)


# need to go to alpha key documents and get the url above for json file

#using parsed_response you can find keys on specific attributes or entire list. This just finds the different values/results.

last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]
now = datetime.datetime.now()
tsd = parsed_response["Time Series (5min)"]
# assuming latest day is first
dates = list(tsd.keys()) # TODO - sort to ensure latest day, time is first
latest_dt = dates[0]# dt = day, time - this gets me the latest item from our list
# dynamically accessing latest data
latest_close = tsd[latest_dt]["4. close"]



# get high price from each day
#high_prices = [10, 20, 30, 5]
#recent_high = max(high_prices)#maximum of all high prices

high_prices = []
low_prices = []

for date in dates:
    high_price = tsd[latest_dt]["2. high"]
    high_prices.append(float(high_price))
    low_price = tsd[latest_dt]["3. low"]
    low_prices.append(float(low_price))
recent_high = max(high_prices)
recent_low = min(low_prices)



# will need to update this (the second portion because this only shows at 1125 on 6.14)
#breakpoint()
# We are determing the different keys we need to process in python - time series daily - based on the day
csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "prices.csv")
with open(csv_file_path, "w") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=["city", "name"])
    writer.writerheader()
    writer.writerow({"city": "New York", "name": "Yankees"})
    writer.writerow({"city": "New York", "name": "Mets"})
    writer.writerow({"city": "Boston", "name": "Red Sox"})
    writer.writerow({"city": "New Haven", "name": "Ravens"})

print("-------------------------")
print("SELECTED SYMBOL: XYZ")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print(f"REQUEST AT: {now}")
print("-------------------------")
print(f"LATEST DAY: {last_refreshed}")#string interprelation using format string
print(f"LATEST CLOSE: {to_usd(float(latest_close))}")
print(f"RECENT HIGH: {to_usd(float(recent_high))}")
print(f"RECENT LOW: {to_usd(float(recent_low))}")
print("-------------------------")
print("RECOMMENDATION: BUY!")# need to design an algorithm to produce recommendation
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("Writing Data to CSV:{csv_file_path}")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")

#csv_file_path = "data/prices.csv"



# write a csv file into the data directory