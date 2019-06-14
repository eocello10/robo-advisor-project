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
