
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