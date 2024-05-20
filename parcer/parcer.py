import requests
from bs4 import BeautifulSoup as BS
r_dota2acc = requests.get("https://funpay.com/lots/81/")
html_dota2acc = BS(r_dota2acc.content, 'html.parser')
offer = html_dota2acc.find("a", class_ = "tc-item")
title = offer.find("div", class_= "tc-desc-text").text.strip()
user = offer.find("div", class_="media-user-name").text.strip()
price = offer.find("div", class_="tc-price").text.strip()
url = html_dota2acc.find("a", class_= "tc-item offer-promo", href=True)["href"].strip()
print(title, user, price, url, sep="\n\n")