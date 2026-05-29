from fastapi.testclient import TestClient
from app.api import app

client = TestClient(app)

def test_analyze_endpoint_returns_stock_analysis():

    response = client.post("/analyze", json = {"ticker": "nvda"})
    data = response.json()

    assert response.status_code == 200
    assert data["ticker"] == "NVDA"
    assert data["overall_sentiment"] == "Positive"
    assert data["positive_headlines"] == 3
    assert data["negative_headlines"] == 2
    assert data["neutral_headlines"] == 0
    assert data["overall_sentiment_score"] == 2
    assert data["price_movement"] == "Up"
    assert data["price_change"] == 8
    assert data["price_change_percent"] == 8.0
    assert data["insight"] == "Positive sentiment matches upward price movement."
    assert len(data["headline_results"]) == 5

    first_result = data["headline_results"][0]
    assert first_result["headline"] == "NVDA reports strong AI chip demand"
    assert first_result["sentiment"] == "Positive"
    assert first_result["positive_word_count"] == 2
    assert first_result["negative_word_count"] == 0
    assert first_result["sentiment_score"] == 2

def test_health_check():

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}