# StockPulse AI

![StockPulse CI](https://github.com/KTP96/AI/actions/workflows/ci.yml/badge.svg)

## Project Overview

StockPulse AI is a beginner-friendly AI + DevOps project that analyzes stock-related news headlines using rule-based sentiment analysis and compares the result with sample stock price movement.

The current version is a command-line Python application. Future versions will add unit tests, FastAPI, Streamlit, Docker, CI/CD, and AWS deployment.

## Features

- Analyze financial news headlines
- Classify each headline as Positive, Negative, or Neutral
- Calculate positive and negative word counts
- Calculate sentiment score for each headline
- Calculate overall stock sentiment
- Calculate sample stock price movement
- Generate a simple insight comparing news sentiment with price movement

## API Endpoints

### GET /health

    - Returns service health status.

    - Example response:

        ```
        {
        "status": "ok"
        }
        ```

### POST /analyze

    - Analyzes stock-related sample headlines and sample price movement.

    - Example request:

        ```
        {
        "ticker": "nvda"
        }
        ```

    - Example response:

        ```
        {
        "ticker": "NVDA",
        "overall_sentiment": "Positive",
        "positive_headlines": 3,
        "negative_headlines": 2,
        "neutral_headlines": 0,
        "overall_sentiment_score": 2,
        "price_movement": "Up",
        "price_change": 8,
        "price_change_percent": 8.0,
        "insight": "Positive sentiment matches upward price movement."
        }
        ```
## Running with Docker

Build the Docker image:

```
docker build -t stockpulse-ai .
```

Run the container:

```
docker run -p 8000:8000 stockpulse-ai
```


Test the health endpoint:

```
curl http://127.0.0.1:8000/health
```

## Running with Docker Compose

Start the service:

```
docker compose up
```

Test the API:

```
curl http://127.0.0.1:8000/health
```

Stop the service:

```
docker compose down
```

## Tech Stack

- Python
- Rule-based NLP
- Git
- GitHub

## How to Run

Run the application from the project root:

```
python app/stockpulse.py
```

## DevOps Progress

- Added pytest-based automated tests for sentiment analysis and price movement logic
- Added GitHub Actions CI workflow to run tests automatically on push to main
- Verified CI pipeline successfully passes on GitHub

## Current Status

- Initial command-line version completed.
- The project currently supports:

    * Rule-based sentiment analysis
    * Sentiment scoring
    * Sample price movement analysis
    * Basic insight generation

## Future Improvements
- Add unit tests using pytest
- Add FastAPI backend
- Add Streamlit dashboard
- Add Docker support
- Add GitHub Actions CI/CD pipeline
- Deploy on AWS EC2
- Add logging and health checks