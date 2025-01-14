import datetime, json, requests, smtplib


STOCK = "REGN"
COMPANY_NAME = "Regeneron Pharma"

# Note: using a JSON rather than environmental variables because I don't want a million API keys I
# probably won't be using again cluttering up the file :)
with open('../info.json') as f:
    contents = json.load(f)
    STOCK_API_KEY = contents['stock_api_key']
    NEWS_API_KEY = contents['news_api_key']
    MY_EMAIL = contents['email']
    MY_PASSWORD = contents['password']


stock_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&outputsize=compact&apikey={STOCK_API_KEY}"
response = requests.get(stock_url).json()


# using while loops is not ideal here, but the stock market is not guaranteed to be closed only on weekends
# e.g. this past Thursday, stock market was closed for mourning former Pres. Carter
# so figured this would be easier for other holidays, especially ones that have moving dates (e.g. Thanksgiving)
yesterday_date = datetime.date.today() - datetime.timedelta(days=1)
yesterday_data = None
while not yesterday_data:
    # Note: Not handling error of calling this API too many times since it will only get called once a day
    yesterday_data = response['Time Series (Daily)'].get(str(yesterday_date))
    if not yesterday_data:
        yesterday_date = yesterday_date - datetime.timedelta(days=1)

day_before_yesterday_date = yesterday_date - datetime.timedelta(days=1)
day_before_yesterday_data = None
while not day_before_yesterday_data:
    day_before_yesterday_data = response['Time Series (Daily)'].get(str(day_before_yesterday_date))
    if not day_before_yesterday_data:
        day_before_yesterday_date = day_before_yesterday_date - datetime.timedelta(days=1)

price_delta = (float(day_before_yesterday_data['4. close']) - float(yesterday_data['4. close']))/float(yesterday_data['4. close'])
SIGNIFICANT_DELTA = 0.05
if price_delta > SIGNIFICANT_DELTA or price_delta < -SIGNIFICANT_DELTA:
    news_url = f"https://newsapi.org/v2/everything?q={COMPANY_NAME}&apiKey={NEWS_API_KEY}"
    response = requests.get(news_url).json()

news_url = f"https://newsapi.org/v2/everything?q={COMPANY_NAME}&apiKey={NEWS_API_KEY}"
articles = requests.get(news_url).json()['articles'][:3]

email_body = f"Subject:Stock alert: {STOCK}: {'🔺' if price_delta > 0 else '🔻'}{round(price_delta*100,0)}%\n\nKey Headlines:"
for article in articles:
    article_content = f"""
    <b>Headline ({article['source']['name']}):</b> {article['title']}
    Brief: {article['description']}
    Read more: {article['url']}
    """
    email_body += article_content

# Send email ^-^ (assignment says to use Twilio but I prefer email)
with smtplib.SMTP('smtp.gmail.com', 587) as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=MY_PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=email_body.encode())