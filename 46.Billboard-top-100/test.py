from bs4 import BeautifulSoup
import requests

url = 'https://www.billboard.com/charts/hot-100/2000-08-12/'

response = requests.get(url)
website_html = response.text

soup = BeautifulSoup(website_html, 'html.parser').prettify()

print(soup)