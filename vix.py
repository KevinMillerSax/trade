import pandas as pd
import pandas_datareader as pdr
import datetime
from datetime import date
import numpy as np

vong = pdr.get_data_yahoo('SPY', start=datetime.datetime(2012,8,1), end=date.today())

vong = vong.reset_index()

df=pd.DataFrame()

df['Date'] = vong.Date
df['Open'] = vong.Open
df['Close'] = vong.Close
df['5MA'] = df.Open.rolling(window=5).mean()
df['20MA'] = df.Open.rolling(window=20).mean()
df['ma_ratio'] = df['5MA'] / df['20MA']
df['buy'] = np.where(df['ma_ratio'] > 1.02, 1, 0)
df['long_profit'] = np.where(df.buy == 1, df.Open.shift(-1).diff(), 0)


print(df)
print(df.long_profit.sum())
print(df.buy.sum())
print(df.long_profit.sum() / df.buy.sum())


