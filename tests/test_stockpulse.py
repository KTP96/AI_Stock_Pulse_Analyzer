from app.stockpulse import analyze_headline_sentiment, calculate_price_change, get_price_movement

def test_positive_headline_sentiment():
    sentiment, pos_word_count, neg_word_count, sentiment_score = analyze_headline_sentiment("NVDA reports strong AI chip demand") 
    assert sentiment == "Positive"
    assert pos_word_count == 2
    assert neg_word_count == 0
    assert sentiment_score == 2

def test_negative_headline_sentiment():
    sentiment, pos_word_count, neg_word_count, sentiment_score = analyze_headline_sentiment("NVDA faces supply chain concerns") 
    assert sentiment == "Negative"
    assert pos_word_count == 0
    assert neg_word_count == 1
    assert sentiment_score == -1

def test_neutral_headline_sentiment():
    sentiment, pos_word_count, neg_word_count, sentiment_score = analyze_headline_sentiment("NVDA announces new AI platform") 
    assert sentiment == "Neutral"
    assert pos_word_count == 0
    assert neg_word_count == 0
    assert sentiment_score == 0

def test_upward_pricemovement():
    price_list = [100, 102, 105, 103, 108]
    price_change, price_change_percent = calculate_price_change(price_list)
    trend = get_price_movement(price_change)
    assert price_change == 8
    assert price_change_percent == 8.0
    assert trend == "Up"

def test_downward_pricemovement():
    price_list = [200, 180]
    price_change, price_change_percent = calculate_price_change(price_list)
    trend = get_price_movement(price_change)
    assert price_change == -20
    assert price_change_percent == -10.0
    assert trend == "Down"

def test_flat_pricemovement():
    price_list = [200, 210, 200]
    price_change, price_change_percent = calculate_price_change(price_list)
    trend = get_price_movement(price_change)
    assert price_change == 0
    assert price_change_percent == 0.0
    assert trend == "Flat"

def test_no_price_pricemovement():
    price_list = []
    price_change, price_change_percent = calculate_price_change(price_list)
    trend = get_price_movement(price_change)
    assert price_change is None
    assert price_change_percent is None
    assert trend == "Invalid price change"

def test_one_val_pricemovement():
    price_list = [100]
    price_change, price_change_percent = calculate_price_change(price_list)
    trend = get_price_movement(price_change)
    assert price_change is None
    assert price_change_percent is None
    assert trend == "Invalid price change"

def test_zero_start_pricemovement():
    price_list = [0, 100]
    price_change, price_change_percent = calculate_price_change(price_list)
    trend = get_price_movement(price_change)
    assert price_change is None
    assert price_change_percent is None
    assert trend == "Invalid price change"


    