from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
import requests
import smtplib

load_dotenv()

smtp_email = os.getenv('SMTP_EMAIL')
password = os.getenv('EMAIL_PASSSWORD')
email = os.getenv('EMAIL_ADDRESS')

header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-GB,de;q=0.8,fr;q=0.6,en;q=0.4,ja;q=0.2",
    "Dnt": "1",
    "Priority": "u=1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Sec-Gpc": "1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0",
}

AMAZON_URL = 'https://appbrewery.github.io/instant_pot/'
LIVE_URL = 'https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6'

response = requests.get(LIVE_URL, headers=header)
website_html = response.text

soup = BeautifulSoup(website_html, 'html.parser')

#print(soup)

price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split('$')[1]
price_as_float = float(price_without_currency)

print(price_as_float)

BUY_PRICE = 100.00

if price_as_float < BUY_PRICE:
    with smtplib.SMTP(os.environ["SMTP_ADDRESS"], port=587) as connection:
        connection.starttls()
        result = connection.login(os.environ["EMAIL_ADDRESS"], os.environ["EMAIL_PASSWORD"])
        connection.sendmail(
            from_addr = os.environ['EMAIL_ADDRESS'],
            to_addrs = os.environ['EMAIL_ADDRESS'],
            msg=f"Subject:Amazon Price Alert!\n\nThe price of the item has dropped to ${price_as_float}.\nCheck it out here: {AMAZON_URL}"
        )