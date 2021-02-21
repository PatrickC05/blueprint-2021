import yfinance
import datetime
import pandas as pd

def getPrices(ticker):
    date = datetime.datetime.today()
    print(date)
    l = yfinance.download(ticker,date-datetime.timedelta(days=30),date,progress=False)
    prices = list(l['Close'])
    return prices
