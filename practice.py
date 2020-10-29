import pandas as pd
import pandas_datareader as pdr
import datetime
from datetime import date
import numpy as np
import matplotlib.pyplot as plt

# OIH XOP etf
# SPY VOO

# vix = pdr.get_data_yahoo('^VIX', start=datetime.datetime(2019,6,1), end=date.today())
oih = pdr.get_data_yahoo('OIH', start=datetime.datetime(2013,6,1), end=datetime.datetime.now())
xop = pdr.get_data_yahoo('XOP', start=datetime.datetime(2013,6,1), end=datetime.datetime.now())

#reset to get date
oih = oih.reset_index()
xop = xop.reset_index()
# uso = uso.reset_index()

#make a chart with date oih xop uso
date = oih.Date
oih_open = oih.Open
xop_open = xop.Open
xop_close = xop.Close
# uso_open = uso.Open

df = pd.DataFrame()

df['Date'] = date
df['oih_open'] = oih_open
df['xop_open'] = xop_open
df['xop_close'] = xop_close
# df['uso_open'] = uso_open

#find the correlations
correlation_xop_oih = df.oih_open.corr(df.xop_open)

#find the ratio
df['Ratio'] = df.xop_open / df.oih_open

# print(df.Ratio)
ratio_mean = df.Ratio.mean()

#calculate rolling average
df['rolling_average'] = df['Ratio'].rolling(window=13).mean()

#caluclate buy based on rolling average
df['buy_xop'] = np.where(df.Ratio > df.rolling_average, 1, 0)

#calulation based on divergence on mean
# df['buy_xop'] = np.where(df.Ratio < (ratio_mean - .003), 1, 0)
# df['short_xop'] = np.where(df.Ratio > (ratio_mean + .003), 1, 0)

print(correlation_xop_oih)
print(ratio_mean)
print(df)

