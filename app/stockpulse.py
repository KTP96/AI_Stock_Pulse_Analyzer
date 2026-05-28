positive_words = ["strong", "growth", "raise", "expands", "demand", "positive", "gain", "profit"]
negative_words = ["concerns", "worry", "loss", "decline", "weak", "risk", "fall", "negative"]

def analyze_headline_sentiment(headline):

    pos_word_count = 0
    neg_word_count = 0

    for word in headline.split():
        if word.lower() in positive_words:
            pos_word_count += 1
        elif word.lower() in negative_words:
            neg_word_count += 1
        
    sentiment_score = pos_word_count - neg_word_count
    sentiment = compare_sentiment_counts(pos_word_count, neg_word_count)

    return sentiment, pos_word_count, neg_word_count, sentiment_score

def analyze_all_headlines(headlines):

    pos_hl_count = 0
    neg_hl_count = 0
    neu_hl_count = 0
    headline_results = []
    overall_score = 0

    for headline in headlines:
        sentiment, pos_word_count, neg_word_count, score = analyze_headline_sentiment(headline)
        headline_results.append(
            {
                "headline": headline,
                "sentiment": sentiment,
                "positive_word_count": pos_word_count,
                "negative_word_count": neg_word_count,
                "sentiment_score": score
            }
        )

        overall_score += score
        if sentiment == "Positive":
            pos_hl_count += 1
        elif sentiment == "Negative":
            neg_hl_count += 1
        else:
            neu_hl_count += 1     

    return pos_hl_count, neg_hl_count, neu_hl_count, overall_score, headline_results
   
def compare_sentiment_counts(pos_hl_count, neg_hl_count):

    if pos_hl_count > neg_hl_count:
        return "Positive"
    elif neg_hl_count > pos_hl_count:
        return "Negative"
    else:
        return "Neutral"
    
def print_headline_results(results):

    for result in results:
        print(f"Headline: {result['headline']}")
        print(f"Sentiment: {result['sentiment']}")
        print(f"Positive Word Count: {result['positive_word_count']}")
        print(f"Negative Word Count: {result['negative_word_count']}")
        print(f"Sentiment Score: {result['sentiment_score']}")
        print()

def print_summary(pos_hl_count, neg_hl_count, neu_hl_count, score, price_movement):

    overall_sentiment = compare_sentiment_counts(pos_hl_count, neg_hl_count)
    insight = generate_insight(overall_sentiment, price_movement)

    print("Overall Summary:")
    print(f"Positive Headlines: {pos_hl_count}")
    print(f"Negative Headlines: {neg_hl_count}")
    print(f"Neutral Headlines: {neu_hl_count}")
    print(f"Overall Sentiment Score: {score}")
    print(f"Overall Stock Sentiment: {overall_sentiment}")
    print(f"Insight: {insight}")
    print()

def print_price_analysis(price_movement, price_change, price_change_percent):

    print("Price Analysis:")
    print(f"Price Movement: {price_movement}")
    print(f"Price Change: {price_change}")
    print(f"Price Change Percentage: {price_change_percent}%")
    print()

def calculate_price_change(prices):

    if len(prices) <= 1 or prices[0] == 0:
        return None, None
    else:
        start_price = prices[0]
        last_price = prices[-1]
        price_change = last_price - start_price
        price_change_percent = (price_change / start_price) * 100

    return price_change, price_change_percent

def get_price_movement(price_change):

    if price_change is None:
        return "Invalid price change"
    else:
        if price_change > 0:
            return "Up"
        elif price_change < 0:
            return "Down"
        else:
            return "Flat"
        
def generate_insight(overall_sentiment, price_movement):
    
    if overall_sentiment == "Positive" and price_movement == "Up":
        return "Positive sentiment matches upward price movement."
    
    elif overall_sentiment == "Negative" and price_movement == "Down":
        return "Negative sentiment matches downward price movement."

    elif overall_sentiment == "Positive" and price_movement == "Down":
        return "Positive sentiment does not match downward price movement."

    elif overall_sentiment == "Negative" and price_movement == "Up":  
        return "Negative sentiment does not match upward price movement."

    elif overall_sentiment == "Neutral" and price_movement == "Flat":
        return "Neutral sentiment matches flat price movement."

    else:
        return "Sentiment and price movement show mixed signals."
      
def main():

    sample_prices = [100, 102, 105, 103, 108]
    price_change, price_change_percent = calculate_price_change(sample_prices)
    price_movement = get_price_movement(price_change)
    stock_ticker = input("Enter the stock ticker:").upper()

    print(f"Analyzing stock: {stock_ticker}\n")

    headlines = [
        "NVDA reports strong AI chip demand",
        "NVDA faces supply chain concerns",
        "Analysts raise NVDA price target",
        "NVDA expands data center business",
        "Investors worry about valuation"
        ]

    pos_hl_count, neg_hl_count, neu_hl_count, overall_score, results = analyze_all_headlines(headlines)

    print_headline_results(results)
    print_summary(pos_hl_count, neg_hl_count, neu_hl_count, overall_score, price_movement)

    print_price_analysis(price_movement, price_change, price_change_percent)
    

if __name__ == "__main__":
    main()
