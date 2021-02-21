import pandas as pd
import datetime

start = datetime.datetime(2017, 1, 1)
end = datetime.datetime(2021, 2, 19)


companies = pd.read_csv('nasdaq_screener_1613925401786.csv')

Symbols = [row['Symbol']
           for index, row in companies.iterrows() if row['Market Cap'] > 1e9]

with open("symbol_list.txt", "w") as text_file:
    for symbol in Symbols:
        text_file.write(symbol+'\n')
