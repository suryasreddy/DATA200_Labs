#Helper Functions

import matplotlib.pyplot as plt
from os import system, name

# Function to Clear the Screen
def clear_screen():
    if name == "nt": # User is running Windows
        _ = system('cls')
    else: # User is running Linux or Mac
        _ = system('clear')

# Function to sort the stock list (alphabetical)
def sortStocks(stock_list):
    try:
        stocks.sort(key=lambda st: st.symbol.upper())  # just in case symbols are lowercase
    except Exception as e:
        print("Sorting stocks failed:", e)

# Function to sort the daily stock data (oldest to newest) for all stocks
def sortDailyData(stock_list):
    for stk in stocks:
        try:
            stk.DataList.sort(key=lambda d: d.date)
        except AttributeError:
            print(f"{stk.symbol} has no DataList")

# Function to create stock chart
def display_stock_chart(stock_list, target_symbol):
        stock_match = next((s for s in stock_list if s.symbol == target_symbol), None)

        if not stock_match:
            print(f"Stock symbol '{target_symbol}' not found.")
            return

        data_points = stock_match.DataList
        if not data_points:
            print(f"No historical data available for {target_symbol}.")
            return

        closing_prices = []
        date_labels = []

        for entry in data_points:
            date_labels.append(entry.date)
            closing_prices.append(entry.close)

        if not closing_prices:
            print("Insufficient data to generate chart.")
            return

        plt.figure(figsize=(11, 6))
        plt.plot(date_labels, closing_prices, linestyle='-', marker='o', linewidth=2)
        plt.title(f"{stock_match.name} ({target_symbol}) - Closing Price History", fontsize=14)
        plt.xlabel("Date", fontsize=12)
        plt.ylabel("Closing Price (USD)", fontsize=12)
        plt.xticks(rotation=30)
        plt.grid(visible=True, linestyle='--', alpha=0.5)
        plt.tight_layout()
        plt.show()
