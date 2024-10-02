# Knowledge-Graph-Construction-and-Causal-Inference
# 📈 Exploring the Impact of Financial News on Stock Prices

**Author**: Shuhan Chen  
**Date**: 2024  
**Project Type**: SURF Research Project  
**Focus**: Knowledge Graph Construction and Causal Inference  
**Target Stock**: Apple Inc. (AAPL)

---

## 📜 Project Overview
This project investigates the relationship between financial news and stock price movements using a combination of **knowledge graph construction** and **causal inference** techniques. The research focuses on analyzing how **Apple Inc.** stock prices are influenced by the financial news cycle, leveraging **web-scraped data**, **natural language processing (NLP)**, and **Granger causality testing**.

The project integrates multiple data science techniques, including:
- **Sentiment analysis** of news articles using NLP.
- **Knowledge graph construction** to map relationships between entities in the financial domain.
- **Causal inference** through Granger causality testing to determine whether financial news sentiment impacts stock prices.

---

## 🔑 Research Questions
1. Can financial news sentiment be quantitatively linked to stock price fluctuations?
2. Is there a causal relationship between published news articles and subsequent movements in Apple’s stock prices?

---

## 🛠️ Methodology

### 1. Data Collection
- **Financial News Data**: Collected using the NewsAPI to gather articles related to Apple Inc. between **July 1, 2024** and **July 31, 2024**.
- **Stock Price Data**: Retrieved from Yahoo Finance API for Apple’s daily close prices over the same period.

```python
# Sample code for stock price data collection
import yfinance as yf

def fetch_stock_data(symbol, period='1mo'):
    stock = yf.Ticker(symbol)
    data = stock.history(period=period)
    return data

stock_data = fetch_stock_data("AAPL")
stock_data.to_csv('apple_stock_data.csv')
