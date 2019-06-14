

# app/robo_advisor.py

import requests
import json
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
latest_close = parsed_response["Time Series (5min)"]["2019-06-14 11:25:00"]["4. close"]
# will need to update this (the second portion because this only shows at 1125 on 6.14)
#breakpoint()
# We are determing the different keys we need to process in python - time series daily - based on the day
print("-------------------------")
print("SELECTED SYMBOL: XYZ")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print(f"REQUEST AT: {now}")
print("-------------------------")
print(f"LATEST DAY: {last_refreshed}")#string interprelation using format string
print(f"LATEST CLOSE: {to_usd(float(latest_close))}")
print("RECENT HIGH: $101,000.00")
print("RECENT LOW: $99,000.00")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")