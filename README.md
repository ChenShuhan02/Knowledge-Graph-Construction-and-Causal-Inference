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


2. Data Preprocessing

• Date Normalization: Align news publication dates with stock price fluctuations for consistent analysis.

Sentiment Analysis: Used TextBlob to quantify sentiment (ranging from -1 to 1) in each news article.

• Entity Extraction: Employed spaCy to extract key entities (organizations, events) from news articles for knowledge graph construction.

# Sample code for sentiment analysis
from textblob import TextBlob

news_data['sentiment'] = news_data['content'].apply(lambda x: TextBlob(x).sentiment.polarity if pd.notnull(x) else 0)

3. Knowledge Graph Construction

• Created a knowledge graph using Neo j to store entities (e.g., companies, products) and relationships (e.g., acquisitions, partnerships) extracted from news content.

• Relation Extraction: Performed subject-verb-object analysis using spaCy's dependency parsing to identify the actions between entities.

4. Causal Inference Analysis

Conducted Granger causality tests to assess if changes in news sentiment "Granger-cause" stock price movements.
# Sample code for Granger causality test
from statsmodels.tsa.stattools import grangercausalitytests

granger_test_data = merged_data[['sentiment', 'Close']].dropna()
grangercausalitytests(granger_test_data, maxlag=3, verbose=True)



* Future Enhancements

1. Expand Data Collection: Extend the data collection period to include more historical data and possibly intraday stock prices.

2. Enhance LP Models: Utilize more sophisticated models such as BERT or FinBERT for better sentiment and entity analysis in financial texts.

3. Refine Causal Analysis: Explore alternative methods such as Vector

Autoregression (VAR) to capture the complexity of financial systems and non-linear relationships.

4. Increase Graph Complexity: Develop more complex relationship extraction techniques to improve the depth of the knowledge graph.
