import datetime, requests, sys
from twilio.rest import Client

STOCK_API_KEY = sys.argv[1]
NEWS_API_KEY = sys.argv[2]
TWILIO_ACCOUNT_SID = sys.argv[3]
TWILIO_AUTH_TOKEN = sys.argv[4]
PHONE_NUMBER = sys.argv[5]

STOCK = "TSLA"
COMPANY_NAME = "Tesla"

UP = "📈"
DOWN = "📉"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
todays_date = str(datetime.date.today()).split("-")
yesterday = "-".join(todays_date[:2] + [str(int(todays_date[-1]) - 1)])
day_before_yesterday = "-".join(todays_date[:2] + [str(int(todays_date[-1]) - 2)])

result = requests.get(
    f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={STOCK_API_KEY}").json()

yesterdays_closing_price = float(result["Time Series (Daily)"][yesterday]["4. close"])
day_before_yesterdays_closing_price = float(result["Time Series (Daily)"][day_before_yesterday]["4. close"])
delta = yesterdays_closing_price / day_before_yesterdays_closing_price

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
if delta < 0.95 or delta > 1.05:
    news_url = 'https://newsapi.org/v2/everything?'
    news_params = {
        "q": COMPANY_NAME,
        "sortBy": "publishedAt",
        "from": yesterday,
        "apiKey": NEWS_API_KEY,
        "language": "en",
        "pagesize": 3,
        "page": 1
    }
    news_response = requests.get(url=news_url, params=news_params).json()['articles']
    if delta < 0.95:
        base_message = f"{STOCK}: {DOWN} {round((1 - delta) * 100)}%\n"
    else:
        base_message = f"{STOCK}: {UP} {round((delta - 1) * 100)}%\n"
    for news in news_response:
        message_body = base_message
        message_body += f"Headline: {news['title']}\n"
        message_body += f"Brief: {news['description']}\n\n"
        print(message_body)
        ## STEP 3: Use https://www.twilio.com
        # Send a seperate message with the percentage change and each article's title and description to your phone number.
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        message = client.messages.create(
            from_='+18885992395',
            body=message_body,
            to=PHONE_NUMBER  # '+16465888715'
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
