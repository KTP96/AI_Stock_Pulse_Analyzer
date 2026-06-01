from fastapi import FastAPI
from pydantic import BaseModel, Field
from app.price import calculate_price_change, get_price_movement
from app.sentiment import analyze_all_headlines, generate_insight, compare_sentiment_counts
import logging

logging.basicConfig(level = logging.INFO)
logger = logging.getLogger(__name__)
app = FastAPI()

class AnalyzeRequest(BaseModel):
    ticker: str = Field(..., min_length = 1)


@app.get("/health")
def health_check():
    logger.info("Health check endpoint called")
    return {"status": "ok"}

@app.post("/analyze")
def analyze_request(request: AnalyzeRequest):
    
    headlines = [
        "NVDA reports strong AI chip demand",
        "NVDA faces supply chain concerns",
        "Analysts raise NVDA price target",
        "NVDA expands data center business",
        "Investors worry about valuation"
    ]
    
    ticker = request.ticker.upper()
    logger.info(f"Analyze endpoint called for ticker: {ticker}")
    
    price_change, price_change_percent = calculate_price_change([100, 102, 105, 103, 108])
    price_movement = get_price_movement(price_change)
    pos_hl_count, neg_hl_count, neu_hl_count, overall_score, headline_results = analyze_all_headlines(headlines)
    overall_sentiment = compare_sentiment_counts(pos_hl_count, neg_hl_count)
    insight = generate_insight(overall_sentiment, price_movement)
    
    return {
        "ticker": ticker,
        "overall_sentiment": overall_sentiment,
        "positive_headlines": pos_hl_count,
        "negative_headlines": neg_hl_count,
        "neutral_headlines": neu_hl_count,
        "overall_sentiment_score": overall_score,
        "price_movement": price_movement, 
        "price_change": price_change,
        "price_change_percent": price_change_percent,
        "insight": insight,
        "headline_results": headline_results
    }
    



