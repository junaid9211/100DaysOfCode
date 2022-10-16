import requests
import os
from bs4 import BeautifulSoup as bs
from twilio.rest import Client

# this simple script texts stock news of tesla to my number if the stock value increases or decreases by 5%
# it uses 3 APIs to work
# API no. 1 alphavantage: API  to grab stock info of Tesla
# API no. 2 newsapi: to grab news about tesla
# API no. 3 twilio: to text me the news of tesla to my phone number

STOCK_API = os.environ['ALPHA_VANTAGE_API']
NEWS_API = os.environ['NEWS_API']

TWILIO_SID = os.environ['TWILIO_ACCOUNT_SID']
TWILIO_AUTH = os.environ['TWILIO_AUTH_TOKEN']

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


def get_perc_change():
    """gets the percentage change of value of tesla stock from yesterday and day before yesterday"""
    stock_params = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': STOCK,
        'apikey': STOCK_API
    }

    stock_response = requests.get(STOCK_ENDPOINT, params=stock_params)
    stock_data = stock_response.json()['Time Series (Daily)']

    iterator = iter(stock_data)
    ytday = next(iterator)
    bf_ytday = next(iterator)

    ytday_close = float(stock_data[ytday]['4. close'])
    bf_ytday_close = float(stock_data[bf_ytday]['4. close'])

    # take the difference and percentage
    diff = ytday_close - bf_ytday_close
    perc_change = round((diff / bf_ytday_close) * 100, 1)

    return perc_change



def get_articles(count):
    """gets news about tesla"""
    news_param = {
        'q': COMPANY_NAME,
        'apiKey': NEWS_API
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_param)
    news_data = news_response.json()['articles']
    top_news = [(bs(item['title'], 'lxml').text, bs(item['description'], 'lxml').text) for item in news_data[:count]]

    return top_news


def send_msg(msg):
    """sends the text message to my number using twilio API"""
    client = Client(TWILIO_SID, TWILIO_AUTH)
    message = client.messages \
        .create(
        body=msg,
        messaging_service_sid='MG6dd65ad170feeee719dc13ca2c4131d4',
        to=os.environ['MY_NUM']
    )
    print('Message sent successfully')

# get the change in percentage
change = get_perc_change()

# if the change is >= 5.0
if abs(change) >= 5.0:

    # see if the change is positive or negative
    if change < 0:
        heading = f"{STOCK}: 🔻{abs(change)}%"
    else:
        heading = f"{STOCK}: 🔺{change}%"

    # get the first article
    top_news = get_articles(1)

    # create the message
    msg = f"{heading}\n"
    i = 1
    for title, description in top_news:
        msg += f"Article No:{i}\n"
        msg += f"Headline: {title}\n"
        msg += f"Brief: {description}\n\n"
        i += 1

    # text me the msg
    send_msg(msg)
