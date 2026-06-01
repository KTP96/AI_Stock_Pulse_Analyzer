import streamlit as st
import requests
import os

st.title("StockPulse AI Dashboard")
st.write("Analyze stock news sentiment and price movement.")

api_url = os.getenv("API_URL", "http://127.0.0.1:8000")

ticker = st.text_input("Enter a stock ticker: ")
analyze_button = st.button("Analyze Stock")

if analyze_button:
    if ticker:
        ticker = ticker.upper()
        try:
            response = requests.post(
                f"{api_url}/analyze",
                json={"ticker": ticker}
            )
            if response.status_code == 200:

                data = response.json()
                st.subheader("Analysis Summary")
                st.success(f"Analysis completed for {data['ticker']}")
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Overall Sentiment", data['overall_sentiment'])
                with col2:
                    st.metric("Overall Sentiment Score", data['overall_sentiment_score'])
                with col3:
                    st.metric("Price Movement", data['price_movement'])

                col4, col5, col6 = st.columns(3)
                with col4:
                    st.metric("Positive Headlines", data['positive_headlines'])
                with col5:
                    st.metric("Price Change", data['price_change'])
                with col6:
                    st.metric("Price Change %",f"{data['price_change_percent']}%")
                
                
                st.write(f"Negative Headlines: {data['negative_headlines']}")
                st.write(f"Neutral Headlines: {data['neutral_headlines']}")
                st.write(f"Insight: {data['insight']}")

                st.subheader("Headline Sentiment Results:")
                st.table(data['headline_results'])
            else:
                st.error(f"API request failed with status code: {response.status_code}")

        except requests.exceptions.ConnectionError:
            st.error("Unable to connect to FastAPI backend. Please start the API server.")
    else:
        st.warning("Please enter the stock ticker.")


