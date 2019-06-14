# robo-advisor-project
Work to pull/suggest stocks to invest in for the end user

-Input the below in your robo-advisor-project.py file:
# app/robo_advisor.py

print("-------------------------")
print("SELECTED SYMBOL: XYZ")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: 2018-02-20 02:00pm")
print("-------------------------")
print("LATEST DAY: 2018-02-20")
print("LATEST CLOSE: $100,000.00")
print("RECENT HIGH: $101,000.00")
print("RECENT LOW: $99,000.00")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")


- User your text editor to create a requirements.txt file. Inpuy the below in there:
requests
python-dotenv

#Environment Setup
Create and activate a new Anaconda virtual environment:

conda create -n stocks-env python=3.7 # (first time only)
conda activate stocks-env
From within the virtual environment, install the required packages specified in the "requirements.txt" file you created:

pip install -r requirements.txt
pip install pytest # (only if you'll be writing tests)
From within the virtual environment, demonstrate your ability to run the Python script from the command-line to check if your code is working properly:

python robo_advisor.py

# Requirements
- Need to take each print item from above and modify them one by one
- Start with importing requests and json in order to use the parsed_response
- Enter the below code. This is where we will get all the stock information required that is updating on a consistent basis:
    request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=5min&apikey=demo"
    response = requests.get(request_url) 
- Create your parsed_response code:
    parsed_response = json.loads(response.text)
- First, start with latest_refershed. You can create a breakpoint (breakpoint()) in your code to allow you to begin to search for the keys from the url.
- to seacrh for the information type in python robo-advisor-project.py. then parsed_response.keys. You will find two: Meta Data and Time Series (5 Min)
- Next step is to find the keys for the Meta Data key. Once you find this you will see the last refreshed is item 3. Use the code below
    - last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]
    - Update print function like this - print(f"LATEST DAY: {last_refreshed}")
- After you will perform the same steps for the Time Series but are required to take a step in between. When finding the keys for the Time Series (parsed_response["Time Series (5min)"] you will see whatever the latest date and time is as the first item. This will be your next key. After that you will see 4. close and this signifies the value you want to pull
    - Be careful we are not finished as we have to create some more dyanimc code in order to get the latest date and time.
        - dates = list(tsd.keys())
        - latest_dt = dates[0]
        - latest_close = tsd[latest_dt]["4. close"]
    - Then update your print statement
        - print(f"LATEST CLOSE: {to_usd(float(latest_close))}")
        - To format (to_usd) us the def function below
            - def to_usd (my_price):
                return "${0:,.2f}".format(my_price)
- Third, we can update the datetime to print whatever it is now
    - import datetime
    - now = datetime.datetime.now()
    - and print(f"REQUEST AT: {now}")

