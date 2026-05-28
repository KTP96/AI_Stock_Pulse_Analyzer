# StockPulse AI Test Plan

## Test Case 1: Positive Headline

Input:
NVDA reports strong AI chip demand

Expected:
Sentiment should be Positive
Positive Word Count should be 2
Negative Word Count should be 0
Sentiment Score should be 2

## Test Case 2: Negative Headline

Input:
NVDA faces supply chain concerns

Expected:
Sentiment should be Negative
Positive Word Count should be 0
Negative Word Count should be 1
Sentiment Score should be -1

## Test Case 3: Neutral Headline

Input:
NVDA announces new AI platform

Expected:
Sentiment should be Neutral
Positive Word Count should be 0
Negative Word Count should be 0
Sentiment Score should be 0

## Test Case 4: Price Movement Up

Input:
[100, 102, 105, 103, 108]

Expected:
Price Change should be 8
Price Change Percentage should be 8.0
Price Movement should be Up