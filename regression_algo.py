import pandas as pd
import quandl
import math


df = quandl.get('WIKI/GOOGL')

data_frame = df[['Open' , 'High', 'Low' , 'Close', 'Volume']]


data_frame_needed = df[['Open', 'Close' , 'Volume']]

forecast_col = 'Close'

data_frame_needed.fillna(-99999 , inplace = True)

forecast_out = int(math.ceil(0.1*len(data_frame_needed)))

data_frame_needed['label'] = data_frame_needed[forecast_col].shift(-forecast_out)

print(data_frame_needed.head())



