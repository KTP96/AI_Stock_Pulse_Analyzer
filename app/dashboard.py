import streamlit as st
import requests



st.title("StockPulse AI Dashboard")
st.write("Analyze stock news sentiment and price movement.")


ticker = st.text_input("Enter a stock ticker: ")
analyze_button = st.button("Analyze Stock")

if analyze_button:
    if ticker:
        ticker = ticker.upper()
        try:
            response = requests.post(
                "http://127.0.0.1:8000/analyze",
                json = {"ticker": ticker}
            )
            data = response.json()
            st.success(f"Analysis completed for {data['ticker']}")
            st.write(f"Overall Sentiment: {data['overall_sentiment']}")
            st.write(f"Price Movement: {data['price_movement']}")
            st.write(f"Insight: {data['insight']}")
        except requests.exceptions.ConnectionError:
            st.error("Unable to connect to FastAPI backend. Please start the API server.")
    else:
        st.warning("Please Enter the stock ticker")


