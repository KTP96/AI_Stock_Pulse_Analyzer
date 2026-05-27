"""
Keep the stock ticker input.
Create one list called headlines.
Store all 5 headlines inside that list.
Print each headline using a for loop.

Expected output
Enter the stock ticker: nvda

Analyzing stock: NVDA

News headlines for NVDA:
1. NVDA reports strong AI chip demand
2. NVDA faces supply chain concerns
3. Analysts raise NVDA price target
4. NVDA expands data center business
5. Investors worry about valuation

"""

headlines=["NVDA reports strong AI chip demand",
     "NVDA faces supply chain concerns",
     "Analysts raise NVDA price target",
     "NVDA expands data center business",
     "Investors worry about valuation"]

stock_ticker=input("Enter the stock ticker:").upper()
print(f"Analyzing stock: {stock_ticker}")

print(f"News headlines for {stock_ticker}")
for i,line in enumerate(headlines):
    print(f"{i+1}. {line}")