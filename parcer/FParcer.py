import requests
from bs4 import BeautifulSoup as BS
r = requests.get("https://funpay.com/lots/221/")
html = BS(r.content, 'html.parser')

sold_dota2 = []
name_dota2 = []
popa = []
for el in html.select(".tc-item"):
	text = el.select(".tc-desc > .tc-desc-text")
	price = el.select(".tc-price > div")
	user = el.select(".media-user-name")
	reviews = el.select(".media-user-reviews")
	user_info = el.select(".media-user-info")
	ob = []
	ob.extend(["Описание: " + text[0].text, "Цена: " + price[0].text, "Продавец: " + user[0].text + "Отзывы: " + reviews[0].text + user_info[0].text])
	popa.append(ob)
print(popa[0][0], "\n", popa[0][1], "\n", popa[0][2], sep='')
