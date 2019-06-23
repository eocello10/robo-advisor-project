# robo-advisor-project
- Work to pull/suggest stocks to invest in for the end user

- Input the below in your robo-advisor-project.py file:
    - app/robo_advisor.py

    - print("-------------------------")
    - print("SELECTED SYMBOL: XYZ")
    - print("-------------------------")
    - print("REQUESTING STOCK MARKET DATA...")
    - print("REQUEST AT: 2018-02-20 02:00pm")
    - print("-------------------------")
    - print("LATEST DAY: 2018-02-20")
    - print("LATEST CLOSE: $100,000.00")
    - print("RECENT HIGH: $101,000.00")
    - print("RECENT LOW: $99,000.00")
    - print("-------------------------")
    - print("RECOMMENDATION: BUY!")
    - print("RECOMMENDATION REASON: TODO")
    - print("-------------------------")
    - print("HAPPY INVESTING!")
    - print("-------------------------")

- User your text editor to create a requirements.txt file. Inpuy the below in there:
requests
python-dotenv

# Environment Setup
- Create and activate a new Anaconda virtual environment:
    - conda create -n stocks-env python=3.7 # (first time only)
    - conda activate stocks-env
- From within the virtual environment, install the required packages specified in the "requirements.txt" file you created:
    - pip install -r requirements.txt
    - pip install pytest # (only if you'll be writing tests)
- From within the virtual environment, demonstrate your ability to run the Python script from the command-line to check if your code is working properly:
- Create an env file to house API_key - ENV file allows you to secure your API Key and let's it be used to invoke the request
- Run python robo_advisor.py

# Requirements

# Imports
- Need to import multiple python modules/packages in order to properly handle the code
    - Datetime - to produce formatted date/time for time requested and latest day of aPI
    - CSV - to process data stored in a csv format
    - Dotenv -allows a program to reference environment variables from a project-specific ".env" file. This makes environment variables much easier to manage, especially for Windows users.
    - JSON - to handle JSON formatting of data
    - Pandas - to handle structured data (i.e. for the API)
    - OS -Use the os module perform command-line-style file and directory operations, and to access system environment variables
# URL Requests

- Enter the below code. This is where we will get all the stock information required that is updating on a consistent basis. As seen below we include in the if statement so it pulls the correct stocks:
    request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=daily&apikey=demo"
    response = requests.get(request_url) 

# API Key
    - You will have to update this code to pull any stock from the API
        - Update MSFT to {symbol} and demo to {API_Key}
    - To get the proper API key (yours) you have to use API_Key = os.environ.get("APLAADVANTAGE_API_KEY"). This will get the API key and enter it as part of the request.

# If Statement
- Then we want to create a if statement loop for inputs to ensure we get proper ones
    - This code below starts the process to get an input: 
        - while True:
            symbol = input("Please enter a stock symbol (i.e. AMZN):")
    - The remainder of your if statement will help to remove invalid inputs. Consider that stocks only have four letter characters as well as no digits.
            - if symbol.isdigit() == True:
                print ('No Numbers can be entered')
            - elif len(symbol) >5:
                print('That symbol seems too long.')
            - else:
                request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_Key}"
                response = requests.get(request_url)
                break
# Parsed Response:
    parsed_response = json.loads(response.text)
- First, start with latest_refershed. You can create a breakpoint (breakpoint()) in your code to allow you to begin to search for the keys from the url.
- to seacrh for the information type in python robo-advisor-project.py. then parsed_response.keys. You will find two: Meta Data and Time Series (5 Min)
- Next step is to find the keys for the Meta Data key. Once you find this you will see the last refreshed is item 3. Use the code below
    - last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]
    - Update print function like this - print(f"LATEST DAY: {last_refreshed}")
- After you will perform the same steps for the Time Series but are required to take a step in between. When finding the keys for the Time Series (parsed_response["Time Series (daily)"] you will see whatever the latest date and time is as the first item. This will be your next key. After that you will see 4. close and this signifies the value you want to pull
    - Be careful we are not finished as we have to create some more dyanimc code in order to get the latest date and time.
        - dates = list(tsd.keys())
        - latest_dt = dates[0]
        - latest_close = tsd[latest_dt]["4. close"]
    - Then update your print statement
        - print(f"LATEST CLOSE: {to_usd(float(latest_close))}")
        - To format (to_usd) us the def function below
            - def to_usd (my_price):
                return "${0:,.2f}".format(my_price)
    - To handle the recent low/recent high code we must use the below:
        high_prices = []
        low_prices = []
        for date in dates:
            high_price = tsd[latest_dt]["2. high"]
            low_price = tsd[latest_dt]["3. low"]
            high_prices.append(float(high_price))
            low_prices.append(float(low_price))

recent_high = max(high_prices)
recent_low = min(low_prices)
- Third, we can update the datetime to print whatever it is now when we requested:
    - now = datetime.datetime.now()
    - and print(f"REQUEST AT: {now}")
    - And to handle the latest close. This allows us to properly format the date and time. If there is a time we use human_friendly_date. If not, we use last_refereshed:
        - if ":" in last_refreshed:
            last_refreshed = pd.to_datetime(last_refreshed)
            Human_friendly_date = last_refreshed.strftime('%b %d %Y %I:%M %p')
        else:
            Human_friendly_date = last_refreshed

# CSV

- In order to get information you request into your CSV file you must use the below:
- This code reflect where we want the information to be stored (which file under which directory name) 
    - csv_file_path = os.path.join(os.path.dirname(__file__), "data", "prices.csv")
- We then format to display the headers we would like to see and write code to get our requests into the CSV file
    - Note: We determined all this information by looking into the API/datframe. We found out where each of the headers were located and how they were structured.
    - csv_headers = ["timestamp", "open", "high", "low", "close", "volume"]
    with open(csv_file_path, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
        writer.writeheader()
        for date in dates:
            daily_prices = tsd[date]
            writer.writerow({
            "timestamp": date,
            "open": daily_prices["1. open"],
            "high": daily_prices["2. high"],
            "low": daily_prices["3. low"],
            "close": daily_prices["4. close"],
            "volume": daily_prices["5. volume"]

# Print Input

- The code below reflects what we print
    - print("-------------------------")
    - print("SELECTED SYMBOL: " + symbol.upper())# Put upper in order to make all symbols reflect as upper
    - print("-------------------------")
    - print("REQUESTING STOCK MARKET DATA...")
    - print(f"REQUEST AT: {now.strftime('%b %d %Y %I:%M %p')}") # formatted date
     - Code/explanation highlighted above under Parsed Response 
    - print("-------------------------")
    - print(f"LATEST DAY: " + Human_friendly_date)#string interprelation using format string
     - Code/explanation highlighted above under Parsed Response
    - print(f"LATEST CLOSE: {to_usd(float(latest_close))}") 
    - print(f"RECENT HIGH: {to_usd(float(recent_high))}")
    - print(f"RECENT LOW: {to_usd(float(recent_low))}")
    - Code/explanation for latest close, recent high, recent low highlighted above under Parsed Response
    - print("-------------------------")
  - Recommendation algorithim
    -  algorithm states that if the latest close is greater than 1.2 multipled byt the recent low we should recommened to buy, if not to sell. I used the same algorithm in order to print the recommendation reason. (had to convert to float in order to make sure syntax with recent_low was same)
        - x = float(latest_close) 
        - if x < recent_low*1.2:
        -     print("RECOMMENDATION: BUY!")
        - else:
        -     print("RECOMMENDATION: SELL!")
        - y = float(latest_close) 
        - if y < recent_low*1.2:
        -     print("RECOMMENDATION REASON: This stocks latest close price is less than 20 percent below its recent low. It is a great opportunity! As Kramer would say Buy!Buy!Buy!")
        - else:
        -     print("RECOMMENDATION REASON: This stocks latest close is greater than 20 percent its recent low. Go make some money and as Kramer would say Sell!Sell!Sell!")
  - The final step is to write the data to the CSV. That is what the below states and what is performed under CSV above 
        - print("-------------------------")
        - print("Writing Data to CSV:{csv_file_path}")
        - print("-------------------------")
        - print("HAPPY INVESTING!")
        - print("-------------------------")

