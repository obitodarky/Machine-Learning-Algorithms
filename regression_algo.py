import pandas as pd
import quandl


df = quandl.get('WIKI/GOOGL')

data_frame = df[['Open' , 'High', 'Low' , 'Close', 'Volume']]


data_frame_needed = df[['Open', 'Close' , 'Volume']]

print(data_frame_needed.head())





