import pandas as pd
import pandas_datareader as pdr
import datetime
import numpy as np

viacB = pdr.get_data_yahoo('VIAC', start=datetime.datetime(2019,8,16), end=datetime.datetime.now())
viacA = pdr.get_data_yahoo('VIACA', start=datetime.datetime(2019,8,16), end=datetime.datetime.now())

#note viacB's volume is MUCH greater than viacA's

viacB = viacB.reset_index()
viacA = viacA.reset_index()

df=pd.DataFrame()
df['Date'] = viacB.Date
df['viacA_open'] = viacA.Open
# df['viacA_close'] = viacA.Close
df['viacB_open'] = viacB.Open
df['viacB_close'] = viacB.Close
df['Ratio'] = viacA.Open / viacB.Open
df['rolling_ratio'] = df['Ratio'].rolling(window=10).mean()
df['buy_viacB'] = np.where(df.Ratio < df.rolling_ratio, 1, 0)
# df['buy_viacA'] = np.where(df.Ratio > df.rolling_ratio, 1, 0)
# df['sell_viacB'] = np.where(df.Ratio > df.rolling_ratio, 1, 0)
df['viacB_long_profit'] = np.where(df.buy_viacB == 1, df.viacB_open.shift(-1).diff(), 0)
# df['viacA_long_profit'] = np.where(df.buy_viacA == 1, df.viacA_open.diff(), 0)
# df['short_profit'] = np.where(df.sell_viacB == 1, df.viacB_open.shift(-1).diff(), 0)

print(df)
print(df.viacB_long_profit.sum())
# print(df.viacA_long_profit.sum())
# print(df.short_profit.sum())
