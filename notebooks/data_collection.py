import yfinance as yf
import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt

tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA']
data = yf.download(tickers, start="2019-01-01", end="2024-12-31", auto_adjust=False)['Adj Close']
data.to_csv("data/stock_prices.csv")

print("Data downloaded and saved!")
data.plot(figsize=(14, 6), title="Stock Prices Over Time")

''' Above code will plot the stock prices with the date on the x-axis and the adjusted close price on the y-axis. Using yfinance to download stock data.
||||||||||||||||||||||||||||||||||||||||||||||||
    The below code will plot the stock prices with the date on the x-axis and the adjusted close price on the y-axis. Uses Alpha Vantage to get intraday data.
'''

ts = TimeSeries(key='TULPYY2Y37TLJZZQ', output_format='pandas')
data, meta = ts.get_intraday(symbol='AAPL', interval='1min', outputsize='compact')
data.to_csv("data/aapl_intraday.csv")

print(data.head())

data['4. close'].plot(figsize=(12, 6), title="AAPL 1-Minute Intraday Prices")
plt.xlabel("Time")
plt.ylabel("Price (USD)")
plt.grid(True)
plt.show()

