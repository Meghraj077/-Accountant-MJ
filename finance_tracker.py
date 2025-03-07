import json
import time
import logging

# Logging setup
logging.basicConfig(filename="finance.log", level=logging.INFO, format="%(asctime)s - %(message)s")

# Sample Finance Data (GST, Income Tax, Stocks)
finance_data = {
    "gst_rate": 18,
    "income_tax_brackets": {
        "0-250000": 0,
        "250001-500000": 5,
        "500001-1000000": 20,
        "1000001-above": 30
    },
    "stocks": {
        "Reliance": 2500,
        "TCS": 3500,
        "Infosys": 1500
    }
}

def calculate_gst(amount):
    gst = (amount * finance_data["gst_rate"]) / 100
    logging.info(f"GST Calculated: ₹{gst} on ₹{amount}")
    return gst

def calculate_income_tax(income):
    tax = 0
    for bracket, rate in finance_data["income_tax_brackets"].items():
        low, high = bracket.split("-")
        low, high = int(low), int(high) if high != "above" else float("inf")
        if income > low:
            taxable_amount = min(income, high) - low
            tax += (taxable_amount * rate) / 100
    logging.info(f"Income Tax Calculated: ₹{tax} on ₹{income}")
    return tax

def get_stock_price(stock_name):
    price = finance_data["stocks"].get(stock_name, "Stock Not Found")
    logging.info(f"Stock Price Checked: {stock_name} - ₹{price}")
    return price

if __name__ == "__main__":
    logging.info("Finance Tracker Started...")
    while True:
        time.sleep(10)  # Every 10 seconds, keep the script running
