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