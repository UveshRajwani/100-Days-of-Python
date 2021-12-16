import requests
import datetime as dt

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
now = dt.datetime.now()
print(now.date())
value = 0
headline = ''
brief = ''
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_api_key = "9LLASFVL0Q9JQZRF"
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={stock_api_key}'
r = requests.get(url)
data = r.json()
data = data['Time Series (Daily)']
yesterday = float(data[f"{now.year}-{now.month}-{now.day - 1}"]['4. close'])
day_before_yesterday = float(data[f"{now.year}-{now.month}-{now.day - 2}"]['4. close'])
difference = (day_before_yesterday - yesterday) / ((day_before_yesterday + yesterday) / 2)
difference = difference * 100
difference = round(difference)

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
def get_news():
    global headline,brief
    news_url = f"https://newsapi.org/v2/everything?q={COMPANY_NAME}&apiKey=cf0850e8bba845c9b4e7b03f0c766c9a"
    n = requests.get(news_url)
    news = n.json()['articles'][0]
    headline = news['title']
    brief = news['description']


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.
from twilio.rest import Client
account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)




if difference > 5 or difference >= -5:
    if difference > 0:
        value = f"🔻{difference}%"
        get_news()
        message = client.messages \
            .create(
            body=f"{STOCK}: {value}\nHeadline:\t{headline}\t({STOCK})\nBrief:\t{brief}",
            from_='+12399325376',
            to='+918200440994'
        )

    else:
        value = f"🔺{difference}%"
        get_news()
        message = client.messages \
            .create(
            body=f"{STOCK}: {value}\nHeadline:\t{headline}\t({STOCK})\nBrief:\t{brief}",
            from_='+12399325376',
            to='+918200440994'
        )

# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
