import yfinance
import datetime
import pandas as pd
from tensorflow import lite
import numpy as np
interpreter = lite.Interpreter(model_path="model.tflite")

interpreter.allocate_tensors()

# Get input and output tensors.
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

def getPrices(ticker):
    date = datetime.datetime.today()
    print(date)
    l = yfinance.download(ticker,date-datetime.timedelta(days=50),date,progress=False)
    prices = list(l['Close'])[-30:]
    input_shape = input_details[0]['shape']
    prices_array = np.array(prices)
    prices_array = prices_array[np.newaxis,...,np.newaxis]
    print(prices_array.shape)
    interpreter.set_tensor(
        input_details[0]['index'], prices_array)

    interpreter.invoke()

    output_days = interpreter.get_tensor(output_details[0]['index'])
    return output_days
