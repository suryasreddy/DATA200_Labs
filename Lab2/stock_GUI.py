import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import stock_data
from stock_class import Stock

class StockGUI:
    def __init__(self, window):
        self.window = window
        self.window.title("SJSU Stock Manager")
        self.stock_list = []

        self.create_widgets()

    def create_widgets(self):
        # === Main Frame for Listbox and Tabs ===
        frame = ttk.Frame(self.window)
        frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # === Stock Listbox ===
        self.stockList = tk.Listbox(frame, height=20, width=30)
        self.stockList.pack(side=tk.TOP, padx=5, pady=5)

        # === Tabs for History and Report ===
        self.tabs = ttk.Notebook(frame)
        self.tabs.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=5, pady=5)

        self.textHistory = tk.Text(self.tabs, height=15, width=60)
        self.tabs.add(self.textHistory, text="History")

        self.textReport = tk.Text(self.tabs, height=15, width=60)
        self.tabs.add(self.textReport, text="Report")

        # === Buttons Frame ===
        button_frame = ttk.Frame(self.window)
        button_frame.pack(side=tk.RIGHT, padx=20, pady=20)

        tk.Button(button_frame, text="Add Stock", command=self.add_stock).pack(pady=5)
        tk.Button(button_frame, text="Buy", command=self.buy_stock).pack(pady=5)
        tk.Button(button_frame, text="Sell", command=self.sell_stock).pack(pady=5)

        # === Menu Bar ===
        menubar = tk.Menu(self.window)
        self.window.config(menu=menubar)

        filemenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="Exit", command=self.window.quit)

        webmenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Web", menu=webmenu)
        webmenu.add_command(label="Scrape Data from Yahoo! Finance...", command=self.scrape_web_data)

        chartmenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Chart", menu=chartmenu)
        chartmenu.add_command(label="Display Chart", command=self.display_chart)

    def add_stock(self):
        symbol = simpledialog.askstring("Input", "Enter Stock Symbol:")
        if not symbol:
            return
        new_stock = Stock(symbol)
        self.stock_list.append(new_stock)
        self.stockList.insert(tk.END, symbol.upper())

    def buy_stock(self):
        try:
            selected = self.stockList.curselection()
            if not selected:
                raise ValueError
            quantity = simpledialog.askinteger("Buy Stock", "Enter quantity to buy:")
            if quantity is None or quantity <= 0:
                raise ValueError
            index = selected[0]
            self.stock_list[index].buy(quantity)
        except:
            messagebox.showerror("Error", "Select a stock and enter a valid number")

    def sell_stock(self):
        try:
            selected = self.stockList.curselection()
            if not selected:
                raise ValueError
            quantity = simpledialog.askinteger("Sell Stock", "Enter quantity to sell:")
            if quantity is None or quantity <= 0:
                raise ValueError
            index = selected[0]
            self.stock_list[index].sell(quantity)
        except:
            messagebox.showerror("Error", "Select a stock and enter a valid number")

    def scrape_web_data(self):
        dateFrom = simpledialog.askstring("Starting Date", "Enter Starting Date (m/d/yy)")
        dateTo = simpledialog.askstring("Ending Date", "Enter Ending Date (m/d/yy)")
        try:
            stock_data.retrieve_stock_web(dateFrom, dateTo, self.stock_list)
        except:
            messagebox.showerror("Cannot Get Data from Web", "Check Path for Chrome Driver")
            return
        self.display_stock_data()
        messagebox.showinfo("Get Data From Web", "Data Retrieved")

    def display_stock_data(self):
        self.textHistory.delete('1.0', tk.END)
        self.textReport.delete('1.0', tk.END)
        for stock in self.stock_list:
            self.textHistory.insert(tk.END, f"{stock.symbol} History:\n")
            for data in stock.history:
                self.textHistory.insert(tk.END, f"{data.date}: Close={data.close}, Volume={data.volume}\n")
            self.textHistory.insert(tk.END, "\n")

            report = stock.get_report()
            self.textReport.insert(tk.END, f"{stock.symbol} Report:\n{report}\n\n")

    def display_chart(self):
        try:
            selection = self.stockList.curselection()
            symbol = self.stockList.get(selection)
            for stock in self.stock_list:
                if stock.symbol == symbol:
                    stock.display_chart()
        except:
            messagebox.showerror("Error", "Select a stock to display chart")


if __name__ == "__main__":
    root = tk.Tk()
    app = StockGUI(root)
    root.mainloop()




