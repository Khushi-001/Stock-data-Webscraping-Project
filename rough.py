import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

def fetch_stock_data(symbol, start_date, end_date):
    stock_data = yf.download(symbol, start_date, end_date)
    return stock_data

def plot_adjusted_close_prices(data):
    data['Adj Close'].plot(figsize=(10, 7))
    plt.legend()
    plt.title("Adjusted Close Price", fontsize=16)
    plt.xlabel("Date", fontsize=16)
    plt.ylabel("Price", fontsize=16)
    plt.grid(which="major", color='k', linewidth=0.5)
    plt.ylim(0)
    plt.show()

def calculate_moving_averages(data, ticker):
    moving_averages_50 = data['Adj Close'].rolling(window=50).mean()
    moving_averages_100 = data['Adj Close'].rolling(window=100).mean()
    
    plt.figure(figsize=(10, 7))
    plt.plot(data.index, data['Adj Close'], label='Price')
    plt.plot(moving_averages_50.index, moving_averages_50, label='MA50')
    plt.plot(moving_averages_100.index, moving_averages_100, label='MA100')
    plt.legend()
    plt.title(f"Adjusted Close Price with Moving Averages - {ticker}", fontsize=16)
    plt.xlabel("Date", fontsize=16)
    plt.ylabel("Price", fontsize=16)
    plt.grid(which="major", color='k', linewidth=0.5)
    plt.ylim(0)
    plt.show()

def plot_volume_analysis(data, ticker):
    plt.figure(figsize=(10, 7))
    plt.subplot(2, 1, 1)
    plt.plot(data.index, data['Adj Close'])
    plt.title("Stock Price")
    plt.xlabel("Date")
    plt.ylabel("Price")
    
    plt.subplot(2, 1, 2)
    plt.plot(data.index, data['Volume'], color='blue')
    plt.title("Trading Volume")
    plt.xlabel("Date")
    plt.ylabel("Volume")
    
    plt.tight_layout()
    plt.show()

def compare_stocks_within_sector(data, tickers_list):
    plt.figure(figsize=(10, 7))
    for ticker in tickers_list:
        plt.plot(data.index, data[ticker], label=ticker)

    plt.title("Stock Prices Comparison - Same Sector", fontsize=16)
    plt.xlabel("Date", fontsize=12)
    plt.ylabel("Price", fontsize=12)
    plt.legend()
    plt.grid(which="major", color='k', linewidth=0.5)
    plt.show()

def save_adjusted_close_price_chart(data, filename):
    data['Adj Close'].plot(figsize=(10, 7))
    plt.legend()
    plt.title("Adjusted Close Price", fontsize=16)
    plt.xlabel("Date", fontsize=16)
    plt.ylabel("Price", fontsize=16)
    plt.grid(which="major", color='k', linewidth=0.5)
    plt.ylim(0)
    plt.savefig(filename)
    plt.show()

def save_candlestick_chart(data, ticker, filename):
    df = data.loc[:, [ticker]]
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(df.index, df[ticker], color='blue', label=ticker)
    ax.set_title(f'Candlestick Chart - {ticker}')
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.legend()
    plt.grid(which="major", color='k', linewidth=0.5)
    plt.savefig(filename)
    plt.show()

# Define the stock symbols and other variables
tickers_list = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'NVDA']
end_date = '2023-01-01'
start_date = '2022-01-01'

# Fetch the stock data
symbol = input("Enter the stock symbol (e.g., AAPL, MSFT, GOOGL, AMZN, NVDA): ")
data = fetch_stock_data(symbol, start_date, end_date)

# Execute desired sections of the code
option = input("Select the type of data visualization:\n1. Adjusted Close Prices\n2. Moving Averages\n3. Volume Analysis\n")
if option == '1':
    plot_adjusted_close_prices(data)
elif option == '2':
    calculate_moving_averages(data, symbol)
elif option == '3':
    plot_volume_analysis(data, symbol)
else:
    print("Invalid option selected.")

# Compare Stocks within the Same Sector
# Plot stock prices of the same sector on the same chart
compare = input("Do you want to compare stock prices within the same sector? (y/n): ")
if compare.lower() == 'y':
    compare_stocks_within_sector(data, tickers_list)

# Save the charts as image files
save_option = input("Do you want to save the charts as image files? (y/n): ")
if save_option.lower() == 'y':
    save_adjusted_close_price_chart(data, 'adjusted_close_price.png')
    save_candlestick_chart(data, symbol, 'candlestick_chart.png')
