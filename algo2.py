#use this to buy
import numpy as np

import yfinance as yf
import pandas as pd
import ta

# Define your list of stocks

from stocks import symbols
stocks=symbols

# Set window size for indicators
WINDOW_SIZE = 100  # default, modify as needed


def add_SMA(df, window=WINDOW_SIZE):
    df['SMA'] = df['Close'].rolling(window).mean()

def add_Bollinger_Bands(df, window=14):
    df['SMA'] = df['Close'].rolling(window).mean()
    df['stddev'] = df['Close'].rolling(window).std()
    df['BB_upper'] = df['SMA'] + (2 * df['stddev'])
    df['BB_lower'] = df['SMA'] - (2 * df['stddev'])

def add_Keltner_Channels(df, window=14):
    df['EMA'] = df['Close'].ewm(span=window).mean()
    df['range'] = df['High'] - df['Low']
    df['KC_upper'] = df['EMA'] + (2 * df['range'].rolling(window).mean())
    df['KC_lower'] = df['EMA'] - (2 * df['range'].rolling(window).mean())

def add_Squeeze(df):
    df['squeeze_on'] = (df['BB_lower'] > df['KC_lower']) & (df['BB_upper'] < df['KC_upper'])


def calculate_indicators(df,window=WINDOW_SIZE):
    # Calculate technical indicators
    df['RSI'] = ta.momentum.RSIIndicator(df['Close']).rsi()
    df['MACD'] = ta.trend.MACD(df['Close']).macd_diff()
    df['BB_High_Indicator'] = ta.volatility.BollingerBands(df['Close']).bollinger_hband_indicator()
    df['BB_Low_Indicator'] = ta.volatility.BollingerBands(df['Close']).bollinger_lband_indicator()
    df['OBV'] = ta.volume.OnBalanceVolumeIndicator(df['Close'], df['Volume']).on_balance_volume()
    df['ATR'] = ta.volatility.AverageTrueRange(df['High'], df['Low'], df['Close']).average_true_range()
    df['stoch_signal'] = ta.momentum.StochasticOscillator(df['High'], df['Low'], df['Close']).stoch_signal()

    # Add Fibonacci retracement levels
    high = df['High'].max()
    low = df['Low'].min()
    diff = high - low
    df['fib_23.6'] = high - 0.236 * diff
    df['fib_38.2'] = high - 0.382 * diff
    df['fib_61.8'] = high - 0.618 * diff

    add_SMA(df, window)
    add_Bollinger_Bands(df, window)
    add_Keltner_Channels(df, window)
    add_Squeeze(df)

def calculate_ratings(df):
    # Assign rating based on indicators
    rating = 0
    if df['RSI'].iloc[-1] < 30:
        rating += 1
    if df['MACD'].iloc[-1] > 0:
        rating += 1
    if df['BB_High_Indicator'].iloc[-1] > 0 or df['BB_Low_Indicator'].iloc[-1] > 0:
        rating += 1
    if df['OBV'].iloc[-1] > df['OBV'].iloc[-2]:
        rating += 1
    if df['ATR'].iloc[-1] < df['ATR'].iloc[-2]:
        rating += 1
    if df['SMA'].iloc[-1] < df['Close'].iloc[-1]:
        rating += 1
    if df['squeeze_on'].iloc[-1]:
        rating += 1
    if df['stoch_signal'].iloc[-1] < 20:
        rating += 1
    if df['Close'].iloc[-1] < df['fib_23.6'].iloc[-1] < df['fib_38.2'].iloc[-1]:
        rating += 1
    return rating

# Fetch stock data and calculate indicators
df_dict = {}

start_data="2022-11-15"
end_date="2023-05-21"
for stock in stocks:
    try:
        df = yf.download(stock, start=start_data, end=end_date)
        calculate_indicators(df)
        df_dict[stock] = df
    except:
        print("problem with a stock data:",stock)
# Calculate ratings for each stock
ratings = {stock: calculate_ratings(df) for stock, df in df_dict.items()}

# Get the stock with the highest rating
best_stock = max(ratings, key=ratings.get)
print(f"The best stock to buy is: {best_stock}")

sorted_dict = dict(sorted(ratings.items(), key=lambda x: x[1], reverse=True))

average = sum(sorted_dict.values()) / len(sorted_dict.values())
