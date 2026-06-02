# StockPulse AI

![StockPulse CI](https://github.com/KTP96/AI/actions/workflows/ci.yml/badge.svg)

## Project Overview

StockPulse AI is an AI + DevOps project that analyzes stock-related news headlines using rule-based sentiment analysis and compares the sentiment result with sample stock price movement.

The project includes a FastAPI backend, Streamlit dashboard, automated pytest test suite, Docker containerization, Docker Compose multi-service setup, GitHub Actions CI, API logging, health checks, and AWS EC2 deployment support.

## Features

* Analyze financial news headlines
* Classify each headline as Positive, Negative, or Neutral
* Calculate positive and negative word counts
* Calculate sentiment score for each headline
* Calculate overall stock sentiment
* Calculate sample stock price movement
* Generate insight comparing news sentiment with price movement
* Expose analysis through FastAPI REST APIs
* Display results in a Streamlit dashboard
* Run backend and dashboard using Docker Compose
* Validate tests, Docker build, and Compose config through GitHub Actions CI

## Tech Stack

* Python
* Rule-based NLP
* FastAPI
* Streamlit
* pytest
* Docker
* Docker Compose
* GitHub Actions
* Git/GitHub
* AWS EC2

## API Endpoints

### GET /health

Returns service health status.

Example response:

```json
{
  "status": "ok"
}
```

### POST /analyze

Analyzes stock-related sample headlines and sample price movement.

Example request:

```json
{
  "ticker": "nvda"
}
```

Example response:

```json
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
  "insight": "Positive sentiment matches upward price movement.",
  "headline_results": [
    {
      "headline": "NVDA reports strong AI chip demand",
      "sentiment": "Positive",
      "positive_word_count": 2,
      "negative_word_count": 0,
      "sentiment_score": 2
    }
  ]
}
```

## How to Run CLI Version

Run the command-line version from the project root:

``` 
python app/stockpulse.py
```

## Run Tests

Run all automated tests:

``` 
python3 -m pytest
```

## Run FastAPI Locally

Start the FastAPI backend:

``` 
uvicorn app.api:app --reload
```

Open Swagger UI:

```  
http://127.0.0.1:8000/docs
```

## Streamlit Dashboard

The project includes a Streamlit dashboard that provides a simple web UI for analyzing stock sentiment and price movement.

The dashboard allows users to:

* Enter a stock ticker
* Call the FastAPI backend
* View overall sentiment
* View price movement
* View sentiment score
* View headline-level sentiment results in a table
* Check backend connection status

### Run Streamlit Locally

Start the FastAPI backend first:

``` 
uvicorn app.api:app --reload
```

Then start the Streamlit dashboard:

``` 
streamlit run app/dashboard.py
```

Open the dashboard:

```  
http://127.0.0.1:8501
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

## Running Full App with Docker Compose

Start both the FastAPI backend and Streamlit dashboard:

``` 
docker compose up --build
```

Open the apps:

```  
FastAPI Swagger UI: http://127.0.0.1:8000/docs
Streamlit Dashboard: http://127.0.0.1:8501
```

Stop the services:

``` 
docker compose down
```

## Architecture

```  
User
 |
 v
Streamlit Dashboard
 |
 v
FastAPI Backend
 |
 v
Sentiment Analysis + Price Movement Logic
```

## Logging

When running with Docker Compose, API logs can be viewed using:

``` 
docker compose logs stockpulse-api
```

Example log messages:

```  
Health check endpoint called
Analyze endpoint called for ticker: NVDA
```

## AWS EC2 Deployment

The application can be deployed on an AWS EC2 Ubuntu instance using Docker Compose.

### EC2 Setup

Install Docker, Docker Compose plugin, and Git:

``` 
sudo apt update
sudo apt install -y docker.io docker-compose-plugin git
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker ubuntu
```

Log out and log back in after adding the user to the Docker group.

### Clone Repository

``` 
git clone https://github.com/KTP96/AI.git
cd AI
```

### Run Application

```
docker compose up --build -d
```

### Verify Containers

```
docker ps
```

Expected containers:

```
stockpulse-api
stockpulse-dashboard
```

### Access Application

Replace `<EC2_PUBLIC_IP>` with the public IP address of the EC2 instance.

```
FastAPI Swagger UI: http://<EC2_PUBLIC_IP>:8000/docs
Streamlit Dashboard: http://<EC2_PUBLIC_IP>:8501
```

### View Logs

```
docker compose logs stockpulse-api
docker compose logs stockpulse-dashboard
```

### Stop Application

```
docker compose down
```

## Current Status

The project currently supports:

* Rule-based sentiment analysis
* Price movement analysis
* FastAPI backend
* Streamlit dashboard
* Dockerized deployment
* Docker Compose multi-service execution
* GitHub Actions CI
* AWS EC2 deployment

## Future Improvements

* Add real stock/news data source
* Add database support
* Add authentication
* Add production-grade monitoring
* Add HTTPS using Nginx or a load balancer
* Push Docker images to GitHub Container Registry
* Automate EC2 deployment from CI/CD
