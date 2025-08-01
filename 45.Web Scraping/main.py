from bs4 import BeautifulSoup

with open('./45.Web Scraping/website.html') as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')

print(soup.prettify())
print(soup.title.string)

all_anchor_tags = soup.find_all(name='a')
for tag in all_anchor_tags:
    print(tag)
    print(tag.getText())
    print(tag.get('href'))