import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "5O4JV1J8XQPK95H5"
NEWS_API_KEY = "5127777e77094325bf78d8e0bb28ffa9"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
stock_parameters = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK_NAME,
    'apikey': STOCK_API_KEY
}
response = requests.get(STOCK_ENDPOINT, params = stock_parameters)
data = response.json()
data_list = [value for (key, value) in data['Time Series (Daily)'].items()]
yesterday_data = data_list[0]
yesterday_closing_price = float(yesterday_data['4. close'])
print(f"Yesterday's closing price: {yesterday_closing_price} $")

#TODO 2. - Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = float(day_before_yesterday_data['4. close'])
print(f"Day before yesterday's closing price: {day_before_yesterday_closing_price} $")

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
positive_difference = abs(yesterday_closing_price - day_before_yesterday_closing_price)
print(f"Positive difference: {positive_difference} $")

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
difference_percentage = (positive_difference / float(day_before_yesterday_closing_price)) * 100
print(f"Percentage difference: {difference_percentage} %")

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if difference_percentage > 0:
    news_parameters = {
        'apiKey': NEWS_API_KEY,
        'q': COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT, params = news_parameters)
    print(news_response.json())
    articles = news_response.json()['articles'][:3]

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
formatted_articles = [
    f"{STOCK_NAME}: {'🔺' if yesterday_closing_price > day_before_yesterday_closing_price else '🔻'}{difference_percentage:.2f}%\n  "
    f"Headline: {article['title']}\n  "
    f"Brief: {article['description']}" for article in articles
]
#TODO 9. - Send each article as a separate message via Twilio. 
print("\n".join(formatted_articles))


#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

