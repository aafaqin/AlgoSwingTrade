# Import necessary libraries
import yfinance as yf
import pandas as pd
from pandas_datareader import data as pdr

# Override pandas_datareader's get_data_yahoo() method with yfinance's implementation
yf.pdr_override()

# List of NSE India stock symbols
symbols = ["RELIANCE.NS", "TCS.NS", "INFY.NS"]  # add as many as you need

symbols = [

"RELIANCE.NS", "TCS.NS", "INFY.NS", "HDFCBANK.NS", "ICICIBANK.NS", "HINDUNILVR.NS", "ITC.NS", "KOTAKBANK.NS", "AXISBANK.NS", "LT.NS", "HDFC.NS", "BAJFINANCE.NS", "MARUTI.NS", "ASIANPAINT.NS", "HCLTECH.NS", "BHARTIARTL.NS", "INDUSINDBK.NS",
    "TATASTEEL.NS", "SBI.NS", "ONGC.NS", "HINDALCO.NS", "WIPRO.NS", "SUNPHARMA.NS", "CIPLA.NS", "JSWSTEEL.NS", "DRREDDY.NS", "POWERGRID.NS", "COALINDIA.NS", "ULTRACEMCO.NS", "TECHM.NS", "IOC.NS", "HEROMOTOCO.NS", "NESTLEIND.NS", "BAJAJFINSV.NS",
    "NTPC.NS", "BRITANNIA.NS", "GRASIM.NS", "BAJAJ-AUTO.NS", "TITAN.NS", "DIVISLAB.NS", "EICHERMOT.NS", "SHREECEM.NS", "ONGC.NS", "UPL.NS", "ADANIPORTS.NS", "HDFCLIFE.NS", "TATACONSUM.NS", "CIPLA.NS", "IOC.NS", "HEROMOTOCO.NS", "NESTLEIND.NS", "BAJAJFINSV.NS",
    "NTPC.NS", "BRITANNIA.NS", "GRASIM.NS", "BAJAJ-AUTO.NS", "TITAN.NS", "DIVISLAB.NS", "EICHERMOT.NS", "SHREECEM.NS", "UPL.NS", "ADANIPORTS.NS", "HDFCLIFE.NS", "TATACONSUM.NS",
"VSTIND.NS", # VST Industries Ltd
"WELSPUNIND.NS", # Welspun India Ltd
"JKLAKSHMI.NS", # JK Lakshmi Cement Ltd
"ARVINDFASN.NS", # Arvind Fashions Ltd
"IDFCFIRSTB.NS", # IDFC First Bank Ltd
"MRPL.NS", # Mangalore Refinery and Petrochemicals Ltd
"RVNL.NS", # Rail Vikas Nigam Ltd
"HIMATSEIDE.NS", # Himatsingka Seide Ltd
"JISLJALEQS.NS", # Jain Irrigation Systems Ltd
"JKTYRE.NS", # JK Tyre & Industries Ltd
"CAREERP.NS", # Career Point Ltd
"ORIENTCEM.NS", # Orient Cement Ltd
"GUJALKALI.NS", # Gujarat Alkalies and Chemicals Ltd
"ALANKIT.NS", # Alankit Ltd
"GODFRYPHLP.NS", # Godfrey Phillips India Ltd
"USHAMART.NS", # Usha Martin Ltd
"VTL.NS", # Vardhman Textiles Ltd
"GPIL.NS", # Godawari Power & Ispat Ltd
"TIINDIA.NS", # Tube Investments of India Ltd
"JKPAPER.NS", # JK Paper Ltd
"BANKBARODA.NS", # Bank of Baroda
"ADANIGREEN.NS", # Adani Green Energy Ltd
"CENTRUM.NS", # Centrum Capital Ltd
"JAYBARMARU.NS", # Jay Bharat Maruti Ltd
"VOLTAMP.NS", # Voltamp Transformers Ltd
"BHEL.NS" # Bharat Heavy Electricals Ltd
]

# Define start and end date
start_date = '2023-04-01'
end_date = '2023-05-20'

# Fetch stock data
stock_data = pdr.get_data_yahoo(symbols, start=start_date, end=end_date)

# Simple strategy: Let's say we consider a stock for buying if it has increased by 5% or more in the last week
buy_stocks = []

for symbol in symbols:
    # Calculate the change in closing price over the last week
    change = (stock_data['Close'][symbol].iloc[-1] - stock_data['Close'][symbol].iloc[-7]) / stock_data['Close'][symbol].iloc[-7]

    # If the change is 5% or more, add the stock to the buy list
    if change >= 0.05:
        buy_stocks.append(symbol)

# Print the stocks to buy
print('Based on the strategy, you should consider buying these stocks in the next week:', ', '.join(buy_stocks))
