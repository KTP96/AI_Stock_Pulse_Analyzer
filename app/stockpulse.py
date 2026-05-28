from app.sentiment import analyze_all_headlines, analyze_headline_sentiment, compare_sentiment_counts, generate_insight
from app.price import get_price_movement, calculate_price_change
    
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
