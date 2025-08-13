from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

house_clone_website = 'https://appbrewery.github.io/Zillow-Clone/'
google_response_link = 'https://docs.google.com/forms/d/e/1FAIpQLSdVtwIsYcQKAwvfoh2Oa6lmiBRa7RAGN95JxQNT4QLFHmyCRA/viewform?usp=sharing&ouid=101246939695271515812'

response = requests.get(house_clone_website, headers=header)
website_html = response.text
soup = BeautifulSoup(website_html, 'html.parser')

# Store all scraped data in lists
all_links = []
all_addresses = []
all_prices = []

property_cards = soup.select(".StyledPropertyCardDataWrapper")

for card in property_cards:
    # Link
    link_tag = card.select_one("a")
    link = link_tag.get("href") if link_tag else None

    # Address
    address_tag = card.select_one("address")
    address = address_tag.get_text(strip=True) if address_tag else None

    # Price
    price_tag = card.select_one(".PropertyCardWrapper span")
    price = price_tag.get_text(strip=True) if price_tag else None
    price_clean = price.replace('/mo', '').split("+")[0] if price else None

    # Append to lists
    all_links.append(link)
    all_addresses.append(address)
    all_prices.append(price_clean)

    print(f"Link: {link}, Address: {address}, Price: {price_clean}")

# Launch Edge browser
edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option('detach', True)
driver = webdriver.Edge(options=edge_options)

# Fill the form for each property
for n in range(len(all_links)):
    driver.get(google_response_link)
    time.sleep(2)

    address_input = driver.find_element(By.XPATH, 
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input = driver.find_element(By.XPATH, 
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_input = driver.find_element(By.XPATH, 
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(By.XPATH, 
        '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')

    address_input.send_keys(all_addresses[n])
    price_input.send_keys(all_prices[n])
    link_input.send_keys(all_links[n])
    submit_button.click()

    time.sleep(1)  # Let the form submit before next iteration