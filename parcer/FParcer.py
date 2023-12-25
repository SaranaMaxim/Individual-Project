import requests
from bs4 import BeautifulSoup as BS
r = requests.get("https://funpay.com/lots/81/")
html = BS(r.content, 'html.parser')

#for el in html.select(".tc-item > .tc-desc"):
#	name = el.select(".tc-desc-text")
#	print(name)
price_dota2 = []
for el in html.select(".tc-item > .tc-price"):
	price = el.select("div")
	price_dota2.append(price[0].text[:-2])
print(price_dota2)
min = 1000000
for el in price_dota2:
	if el < min:
		min = el
print(min)

