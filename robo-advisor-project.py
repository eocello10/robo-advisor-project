

# app/robo_advisor.py


import csv
import json
import os

from dotenv import load_dotenv
import requests

import datetime

load_dotenv()
# need to check with prof about dot_env issue

def to_usd (my_price):
   return "${0:,.2f}".format(my_price)
#
#Info inputs
#

API_Key = os.environ.get("APLAADVANTAGE_API_KEY") # API KEY SHOULD BE READ FROM ENV FILE. NEED TO FIND
# need to pip install python-dotenv

 # TODO: ask user for this

while True:
    symbol = input("Please enter a stock symbol (i.e. AMZN):")
    if symbol.isdigit() == True:
        print ('No Numbers can be entered')
    elif len(symbol) >5:
        print('That symbol seems too long.')
    else:
        request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_Key}"
        response = requests.get(request_url)
        break

parsed_response = json.loads(response.text)
try:
    parsed_response['Time Series (Daily)']
except:
    print('Looks like that is not a valid Stock Symbol. Please restart!')
    print('Shutting program down...')
    exit()
# ask about how this code works
# need to find a way to remove random sybols (i.e. ??)


 
#print(type(response))#<class 'requests.models.Response'>
#print(response.status_code)#>200
#print(response.text)#




# need to go to alpha key documents and get the url above for json file

#using parsed_response you can find keys on specific attributes or entire list. This just finds the different values/results.

last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]
now = datetime.datetime.now()
tsd = parsed_response["Time Series (Daily)"]
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
    low_price = tsd[latest_dt]["3. low"]
    high_prices.append(float(high_price))
    low_prices.append(float(low_price))

recent_high = max(high_prices)
recent_low = min(low_prices)



# will need to update this (the second portion because this only shows at 1125 on 6.14)

# We are determing the different keys we need to process in python - time series daily - based on the day
csv_file_path = os.path.join(os.path.dirname(__file__), "data", "prices.csv")

csv_headers = ["timestamp", "open", "high", "low", "close", "volume"]
#breakpoint()
with open(csv_file_path, "w") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
    writer.writeheader()
    #I think i have to create a prices.csv file?
    for date in dates:
        daily_prices = tsd[date]
        writer.writerow({
        "timestamp": date,
        "open": daily_prices["1. open"],
        "high": daily_prices["2. high"],
        "low": daily_prices["3. low"],
        "close": daily_prices["4. close"],
        "volume": daily_prices["5. volume"]
    })
# looping to write each row
print("-------------------------")
print("SELECTED SYMBOL: " + symbol.upper())
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print(f"REQUEST AT: {now.strftime('%b %d %Y %I:%M %p')}") # need to use format I used previosuly for time
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

#The selected stock symbol(s) (e.g. "Stock: MSFT") - Complete
#The date and time when the program was executed, formatted in a human-friendly way (e.g. "Run at: 11:52pm on June 5th, 2018") - Complete
#The date when the data was last refreshed, usually the same as the latest available day of daily trading data (e.g. "Latest Data from: June 4th, 2018") - Complete
#For each stock symbol: its latest closing price, its recent high price, and its recent low price, calculated according to the instructions below, and formatted as currency with a dollar sign and two decimal places with a thousands separator as applicable (e.g. "Recent High: $1,234.56", etc.) - Complete
#A recommendation as to whether or not the client should buy the stock (see guidance below), and optionally what quantity to purchase. The nature of the recommendation for each symbol can be binary (e.g. "Buy" or "No Buy"), qualitative (e.g. a "Low", "Medium", or "High" level of confidence), or quantitative (i.e. some numeric rating scale).
#A recommendation explanation, describing in a human-friendly way the reason why the program produced the recommendation it did (e.g. "because the stock's latest closing price exceeds threshold XYZ, etc...")