import os

API_KEY = os.environ["ALPHAVANTAGE_API_KEY"]
IBM_URL = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=IBM&apikey={API_KEY}"
APPLE_URL = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=AAPL&apikey={API_KEY}'
VARIABLE_DICT = {"open_price":"1. open","close_price":"4. close","volume":"6. volume","time_series_daily":"Time Series (Daily)"}
IBM_SYMBOL = "IBM"
APPLE_SYMBOL = "Apple Inc."