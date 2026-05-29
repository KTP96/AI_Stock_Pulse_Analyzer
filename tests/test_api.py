from fastapi.testclient import TestClient
from app.api import app

client = TestClient(app)

def test_analyze_endpoint_returns_uppercase_ticker():

    response = client.post("/analyze", json = {"ticker": "nvda"})
    data = response.json()

    assert response.status_code == 200
    assert data["ticker"] == "NVDA"
    assert data["overall_sentiment"] == "Positive"
    assert data["price_movement"] == "Up"
    assert data["price_change"] == 8
    assert data["price_change_percent"] == 8.0
    assert data["insight"] == "Positive sentiment matches upward price movement."

def test_health_check():

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}