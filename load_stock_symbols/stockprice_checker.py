from numpy.core.numeric import NaN
import pandas as pd
import math
stocks = pd.read_csv('load_stock_symbols/stock_dataframe.csv')
for index, row in stocks.iterrows():
    if math.isnan(row['Close']):
        print(row)

print('finished')
