import pandas as pd
import pandas_datareader as pdr
import datetime
import matplotlib.pyplot as plt

aapl = pdr.get_data_yahoo('AAPL', start=datetime.datetime(2008,1,1), end=datetime.datetime(2012,1,1))
aapl.describe()

aapl['Change'] = aapl.Open - aapl.Close
aapl['Pct_Chg'] = aapl.Change / aapl.Open
aapl.to_csv('aapl_02_04.csv')
download_aapl="02_04CSV.csv"

aapl['Pct_Chg'].plot(grid=True)
plt.show()

def get(tickers, startDate, endDate):
  def data(ticker):
    return(pdr.get_data_yahoo(ticker, start=startDate, end=endDate))
  datas = map(data, tickers)
  return(pd.concat(datas, keys=tickers, names=['Ticker', 'Date']))

tickers=['MSFT', 'INTC', 'GOOG', 'KO']
all_data = get(tickers, datetime.datetime(2015,1,1), datetime.datetime(2019,1,1))

all_data.to_csv('four_tickers.csv')
download_all_data='four_tickersCSV.csv'