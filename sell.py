#use this to sell stocks

import yfinance as yf
import pandas as pd
import ta
import numpy as np

# Define your list of stocks
from stocks import symbols
stocks=symbols

def add_SMA(df, window=14):
    df['SMA'] = df['Close'].rolling(window).mean()

def calculate_indicators(df):
    # Calculate technical indicators
    df['RSI'] = ta.momentum.RSIIndicator(df['Close']).rsi()
    df['MACD'] = ta.trend.MACD(df['Close']).macd_diff()
    df['Signal'] = ta.trend.MACD(df['Close']).macd_signal()
    add_SMA(df)

def calculate_sell_ratings(df):
    # Assign rating based on indicators
    rating = 0
    if df['RSI'].iloc[-1] > 70:
        rating += 1
    if df['MACD'].iloc[-1] < df['Signal'].iloc[-1]:
        rating += 1
    if df['Close'].iloc[-1] < df['SMA'].iloc[-1]:
        rating += 1
    return rating

# Fetch stock data and calculate indicators
df_dict = {}
for stock in stocks:
    df = yf.download(stock, start="2023-04-01", end="2023-05-21")
    calculate_indicators(df)
    df_dict[stock] = df

# Calculate sell ratings for each stock
sell_ratings = {stock: calculate_sell_ratings(df) for stock, df in df_dict.items()}

# Get the stock with the highest sell rating
stock_to_sell = max(sell_ratings, key=sell_ratings.get)

# Check the sell rating
if sell_ratings[stock_to_sell] >= 2:  # This threshold can be adjusted based on your strategy
    print(f"It's time to sell {stock_to_sell}.")
else:
    print(f"It's not yet time to sell {stock_to_sell}.")
