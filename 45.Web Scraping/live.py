# Scraping a live website
import requests
from bs4 import BeautifulSoup

response = requests.get('https://news.ycombinator.com/news')
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
articles = soup.find_all(name='a', class_='storylink')
articles_text = []
articles_link = []
for article_tag in articles:
    text = article_tag.getText()
    articles_text.append(text)
    link = article_tag.get('href')
    articles_link.append(link)

articles_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name='span', class_='score')]

largest_number = max(articles_upvote)
largest_index = articles_upvote.index(largest_number)

print(articles_text[largest_index])
print(articles_link[largest_index])