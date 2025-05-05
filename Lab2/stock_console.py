# Summary: This module contains the user interface and logic for a console-based version of the stock manager program.

from datetime import datetime
from stock_class import Stock, DailyData
from utilities import clear_screen, display_stock_chart
from os import path
import stock_data

# Main Menu
def main_menu(stock_list):
    option = ""
    while option != "0":
        clear_screen()
        print("Stock Analyzer ---")
        print("1 - Manage Stocks (Add, Update, Delete, List)")
        print("2 - Add Daily Stock Data (Date, Price, Volume)")
        print("3 - Show Report")
        print("4 - Show Chart")
        print("5 - Manage Data (Save, Load, Retrieve)")
        print("0 - Exit Program")
        option = input("Enter Menu Option: ")
        while option not in ["1","2","3","4","5","0"]:
            clear_screen()
            print("*** Invalid Option - Try again ***")
            option = input("Enter Menu Option: ")
        if option == "1":
            manage_stocks(stock_list)
        elif option == "2":
            add_stock_data(stock_list)
        elif option == "3":
            display_report(stock_list)
        elif option == "4":
            display_chart(stock_list)
        elif option == "5":
            manage_data(stock_list)
        else:
            clear_screen()
            print("Goodbye")

# Manage Stocks
def manage_stocks(stock_list):
    option = ""
    while option != "0":
        clear_screen()
        print("Manage Stocks ---")
        print("1 - Add Stock")
        print("2 - Update Shares")
        print("3 - Delete Stock")
        print("4 - List Stocks")
        print("0 - Exit Manage Stocks")
        option = input("Enter Menu Option: ")
        if option == "1":
            add_stock(stock_list)
        elif option == "2":
            update_shares(stock_list)
        elif option == "3":
            delete_stock(stock_list)
        elif option == "4":
            list_stocks(stock_list)

# Add new stock to track
def add_stock(stock_list):
    clear_screen()
    print("=== Add New Stock ===")
    
    symbol = input("Stock Ticker (e.g., TSLA): ").strip().upper()
    name = input("Company Name: ").strip()
    
    try:
        shares = float(input("Number of Shares: "))
    except ValueError:
        print("Invalid input. Shares must be a number.")
        input("Press Enter to continue...")
        return

    new_stock = Stock(symbol, name, shares)
    stock_list.append(new_stock)
    
    print(f"{symbol} successfully added to your portfolio.")
    input("Press Enter to continue...")

# Buy or Sell Shares Menu
def update_shares(stock_list):
    clear_screen()
    print("=== Buy/Sell Shares ===")
    
    symbol = input("Enter Stock Symbol: ").strip().upper()
    stock = next((s for s in stock_list if s.symbol == symbol), None)

    if not stock:
        print("No matching stock found.")
        input("Press Enter to continue...")
        return

    action = input("Type B to Buy or S to Sell: ").strip().upper()
    try:
        quantity = float(input("How many shares?: "))
    except ValueError:
        print("Invalid number.")
        input("Press Enter to continue...")
        return

    if action == 'B':
        stock.buy(quantity)
        print(f"{quantity} shares bought.")
    elif action == 'S':
        stock.sell(quantity)
        print(f"{quantity} shares sold.")
    else:
        print("Invalid option.")
    
    input("Press Enter to continue...")

# Remove stock and all daily data
def delete_stock(stock_list):
    clear_screen()
    print("=== Delete Stock ===")
    
    symbol = input("Stock Symbol to Remove: ").strip().upper()
    stock_to_remove = next((s for s in stock_list if s.symbol == symbol), None)

    if stock_to_remove:
        stock_list.remove(stock_to_remove)
        print(f"{symbol} was successfully removed.")
    else:
        print("Stock not found.")
    
    input("Press Enter to continue...")

# List stocks being tracked
def list_stocks(stock_list):
    clear_screen()
    print("=== Stocks in Portfolio ===")
    
    if not stock_list:
        print("No stocks currently being tracked.")
    else:
        for s in stock_list:
            print(f"{s.symbol} - {s.name} | {s.shares:.2f} shares")
    
    input("Press Enter to continue...")

# Add Daily Stock Data
def add_stock_data(stock_list):
    clear_screen()
    print("=== Add Daily Stock Data ===")
    
    symbol = input("Stock Symbol: ").strip().upper()
    stock = next((s for s in stock_list if s.symbol == symbol), None)

    if not stock:
        print("Stock not found.")
        input("Press Enter to continue...")
        return

    try:
        date = datetime.strptime(input("Date (m/d/yy): "), "%m/%d/%y")
        close = float(input("Closing Price: "))
        volume = float(input("Volume: "))
    except ValueError:
        print("Invalid input. Please enter correct formats.")
        input("Press Enter to continue...")
        return

    stock.add_data(DailyData(date, close, volume))
    print("Daily data added successfully.")
    input("Press Enter to continue...")

# Display Report for All Stocks
def display_report(stock_list):
    clear_screen()
    print("=== Portfolio Report ===")
    
    for stock in stock_list:
        print(f"{stock.symbol} - {stock.name} | Shares: {stock.shares}")
        for entry in stock.DataList:
            date_str = entry.date.strftime("%m/%d/%y")
            print(f"  {date_str} | Close: ${entry.close:.2f} | Vol: {int(entry.volume)}")
        print("-" * 40)
    
    input("Press Enter to continue...")
# Display Chart
def display_chart(stock_list):
    clear_screen()
    print("=== Display Chart ===")

    symbol = input("Enter Stock Symbol: ").strip().upper()
    display_stock_chart(stock_list, symbol)

    input("Press Enter to continue...")

# Manage Data Menu
def manage_data(stock_list):
    option = ""
    while option != "0":
        clear_screen()
        print("Manage Data ---")
        print("1 - Save Data")
        print("2 - Load Data")
        print("3 - Retrieve from Web")
        print("4 - Import CSV File")
        print("0 - Return to Main Menu")
        option = input("Enter Menu Option: ")
        if option == "1":
            stock_data.save_stock_data(stock_list)
            print("Data saved.")
        elif option == "2":
            stock_data.load_stock_data(stock_list)
            print("Data loaded.")
        elif option == "3":
            retrieve_from_web(stock_list)
        elif option == "4":
            import_csv(stock_list)
        input("Press Enter to continue...")

# Retrieve stock price and volume history from Yahoo! Finance using Web Scraping
def retrieve_from_web(stock_list):
    clear_screen()
    print("=== Web Data Retrieval ===")
    
    start_date = input("Start Date (MM/DD/YY): ")
    end_date = input("End Date (MM/DD/YY): ")
    
    print("\nAttempting to fetch stock history...\n")
    
    try:
        total = stock_data.retrieve_stock_web(start_date, end_date, stock_list)
        print(f"Success! Retrieved {total} data points.")
    except Exception as err:
        print(f"Error: Unable to retrieve data.\nDetails: {err}")
    
    input("\n[Enter] to continue...")

# Import stock price and volume history from Yahoo! Finance using CSV Import
def import_csv(stock_list):
    clear_screen()
    print("=== Import from CSV ===")

    stock_symbol = input("Provide stock ticker (e.g., AAPL): ")
    path_to_file = input("Full path to CSV file: ")

    print(f"\nLoading data from: {path_to_file}")

    try:
        stock_data.import_stock_web_csv(stock_list, stock_symbol, path_to_file)
        print("✔️  Import successful.")
    except FileNotFoundError:
        print("File not found. Please check the path and try again.")
    except Exception as ex:
        print(f"Failed to import data. Reason: {ex}")
    
    input("\n[Enter] to continue...")

# Begin program
def main():
    #check for database, create if not exists
    if path.exists("stocks.db") == False:
        stock_data.create_database()
    stock_list = []
    main_menu(stock_list)

# Program Starts Here
if __name__ == "__main__":
    # execute only if run as a stand-alone script
    main()

