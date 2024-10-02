import requests
import pandas as pd

api_key = 'e13f6b18ab0f42839f5408566063629a'

# 搜索关键词
query = 'Apple'

# 指定时间范围
from_date = '2024-06-30'
to_date = '2024-07-30'

# 新闻数据 URL
news_url = (
    f'https://newsapi.org/v2/everything?q={query}&from={from_date}&to={to_date}&'
    f'sortBy=publishedAt&language=en&apiKey={api_key}'
)

# 获取新闻数据
response = requests.get(news_url)
data = response.json()

# 检查是否成功获取数据
if 'articles' in data:
    articles = data['articles']
    news_df = pd.DataFrame(articles)
    print(news_df.head())

    # 保存数据为 CSV 文件
    news_df.to_csv('apple_news_data.csv', index=False)
else:
    print(f"Error fetching data: {data.get('message', 'Unknown error')}")



import pandas as pd
import yfinance as yf
import statsmodels.api as sm
import numpy as np
from GoogleNews import GoogleNews
import ssl
from datetime import datetime, timedelta

# 忽略SSL证书验证
ssl._create_default_https_context = ssl._create_unverified_context

def fetch_company_news():
    googlenews = GoogleNews(lang='en')
    googlenews.search('Apple Inc.')
    news_data = googlenews.results()
    news_items = []
    for news in news_data:
        try:
            date_str = news['date']
            if 'hour' in date_str:
                date = datetime.now().date()
            elif 'day' in date_str:
                days_ago = int(date_str.split()[0])
                date = (datetime.now() - timedelta(days=days_ago)).date()
            else:
                date = pd.to_datetime(date_str).date()

            news_items.append({
                'title': news['title'],
                'link': news['link'],
                'date': date
            })
        except Exception as e:
            print(f"Error parsing news item: {e}")
    return news_items

def fetch_stock_data(symbol, period='1y'):
    stock = yf.Ticker(symbol)
    data = stock.history(period=period)
    return data

# 获取苹果公司股票数据
stock_data = fetch_stock_data("AAPL")
if not stock_data.empty:
    stock_data.to_csv('apple_stock_data.csv')
else:
    print("No stock data fetched.")

import pandas as pd



