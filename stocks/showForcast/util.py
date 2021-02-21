from os import getpgid
import yfinance
import datetime
from tensorflow import lite
import numpy as np
import time
interpreter = lite.Interpreter(model_path="model.tflite")

interpreter.allocate_tensors()

# Get input and output tensors.
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()


def getPrices(ticker):
    date = datetime.datetime.today()
    s = yfinance.download(
        ticker, date-datetime.timedelta(days=1510), date, progress=False)
    long_arr = np.array(list(s['Close']))
    mean = np.mean(long_arr)
    std = np.std(long_arr)
    l = yfinance.download(
        ticker, date-datetime.timedelta(days=50), date, progress=False)
    prices = list(l['Close'])[-30:]
    prices_array = np.array(prices)
    prices_array = prices_array.astype('float32')
    prices_array = (prices_array-mean)/std
    result = list(np.copy(prices_array))
    prices_array = prices_array[np.newaxis, ..., np.newaxis]
    for i in range(7):
        interpreter.set_tensor(
            input_details[0]['index'], prices_array)
        interpreter.invoke()
        prices_array = interpreter.get_tensor(output_details[0]['index'])
        result.append(prices_array[0, -1, 0])
    return [i*std+mean for i in result]
