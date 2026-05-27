"""
Use your original headlines list:

NVDA reports strong AI chip demand
NVDA faces supply chain concerns
Analysts raise NVDA price target
NVDA expands data center business
Investors worry about valuation

For each headline:

Print the headline.
Print sentiment for that headline.
Overall Sentiment

"""
stock_ticker=input("Enter the stock ticker:").upper()
print(f"Analyzing stock: {stock_ticker}\n")

print(f"News headlines for {stock_ticker}:\n ")

positive_words=["strong", "growth", "raise", "expands", "demand", "positive", "gain", "profit"]
negative_words=["concerns", "worry", "loss", "decline", "weak", "risk", "fall", "negative"]
headlines=["NVDA reports strong AI chip demand",
     "NVDA faces supply chain concerns",
     "Analysts raise NVDA price target",
     "NVDA expands data center business",
     "Investors worry about valuation"]
pos_hl_count=0
neg_hl_count=0
neu_hl_count=0

for headline in headlines:
    pos_word_count=0
    neg_word_count=0
    print(f"Headline: {headline}")
    for word in headline.split():
        if word.lower() in positive_words:
            pos_word_count+=1
        elif word.lower() in negative_words:
            neg_word_count+=1
    if pos_word_count>neg_word_count:
        print("Sentiment: Positive")
        pos_hl_count+=1
    elif neg_word_count>pos_word_count:
        print("Sentiment: Negative")
        neg_hl_count+=1
    else:
        print("Sentiment: Neutral")
        neu_hl_count+=1
    
    print()
print("Overall Summary")
print(f"Positive Headlines: {pos_hl_count}")
print(f"Negative Headlines: {neg_hl_count}")
print(f"Neutral Headlines: {neu_hl_count}")

if pos_hl_count>neg_hl_count:
    print("Overall Stock Sentiment: Positive")
elif neg_hl_count>pos_hl_count:
    print("Overall Stock Sentiment: Negative")
else:
    print("Overall Stock Sentiment: Neutral")




