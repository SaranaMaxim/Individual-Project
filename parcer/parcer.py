import requests
from bs4 import BeautifulSoup as BS
def dota2():
	r_dota2acc = requests.get("https://funpay.com/lots/81/")
	html_dota2acc = BS(r_dota2acc.content, 'html.parser')
	accounts_dota2 = []
	for el in html_dota2acc.select(".tc-item"):
		text = el.select(".tc-desc > .tc-desc-text")
		price = el.select(".tc-price > div")
		user = el.select(".media-user-name")
		reviews = el.select(".media-user-reviews")
		user_info = el.select(".media-user-info")
		object_dota2 = []
		object_dota2.extend(["Описание: " + text[0].text, "Цена: " + price[0].text, "Продавец: " + user[0].text + "Отзывы: " + reviews[0].text + user_info[0].text])
		accounts_dota2.append(object_dota2)
	#print(accounts_dota2[0][0], "\n", accounts_dota2[0][1], "\n", accounts_dota2[0][2], sep='')
	r_dota2priv = requests.get("https://funpay.com/lots/867/")
	html_dota2priv = BS(r_dota2priv.content, 'html.parser')
	priv_dota2 = []
	for el in html_dota2priv.select(".tc-item"):
		text = el.select(".tc-desc > .tc-desc-text")
		price = el.select(".tc-price > div")
		user = el.select(".media-user-name")
		reviews = el.select(".media-user-reviews")
		user_info2 = el.select(".media-user-info")
		object_dota2 = []
		object_dota2.extend(["Описание: " + text[0].text, "Цена: " + price[0].text, "Продавец: " + user[0].text + "Отзывы: " + reviews[0].text + user_info[0].text])
		priv_dota2.append(object_dota2)

	r_dota2predm = requests.get("https://funpay.com/lots/210/")
	html_dota2predm = BS(r_dota2predm.content, 'html.parser')
	predm_dota2 = []
	for el in html_dota2predm.select(".tc-item"):
		text = el.select(".tc-desc > .tc-desc-text")
		price = el.select(".tc-price > div")
		user = el.select(".media-user-name")
		reviews = el.select(".media-user-reviews")
		user_info = el.select(".media-user-info")
		object_dota2 = []
		object_dota2.extend(["Описание: " + text[0].text, "Цена: " + price[0].text, "Продавец: " + user[0].text + "Отзывы: " + reviews[0].text + user_info[0].text])
		predm_dota2.append(object_dota2)

	r_dota2boost = requests.get("https://funpay.com/lots/82/")
	html_dota2boost = BS(r_dota2boost.content, 'html.parser')
	boost_dota2 = []
	for el in html_dota2boost.select(".tc-item"):
		text = el.select(".tc-desc > .tc-desc-text")
		price = el.select(".tc-price > div")
		user = el.select(".media-user-name")
		reviews = el.select(".media-user-reviews")
		user_info = el.select(".media-user-info")
		object_dota2 = []
		object_dota2.extend(["Описание: " + text[0].text, "Цена: " + price[0].text, "Продавец: " + user[0].text + "Отзывы: " + reviews[0].text + user_info[0].text])
		boost_dota2.append(object_dota2)

	r_dota2kal = requests.get("https://funpay.com/lots/500/")
	html_dota2kal = BS(r_dota2kal.content, 'html.parser')
	kal_dota2 = []
	for el in html_dota2kal.select(".tc-item"):
		text = el.select(".tc-desc > .tc-desc-text")
		price = el.select(".tc-price > div")
		user = el.select(".media-user-name")
		reviews = el.select(".media-user-reviews")
		user_info = el.select(".media-user-info")
		object_dota2 = []
		object_dota2.extend(["Описание: " + text[0].text, "Цена: " + price[0].text, "Продавец: " + user[0].text + "Отзывы: " + reviews[0].text + user_info[0].text])
		kal_dota2.append(object_dota2)

	r_dota2lp = requests.get("https://funpay.com/lots/501/")
	html_dota2lp = BS(r_dota2lp.content, 'html.parser')
	lp_dota2 = []
	for el in html_dota2lp.select(".tc-item"):
		text = el.select(".tc-desc > .tc-desc-text")
		price = el.select(".tc-price > div")
		user = el.select(".media-user-name")
		reviews = el.select(".media-user-reviews")
		user_info = el.select(".media-user-info")
		object_dota2 = []
		object_dota2.extend(["Описание: " + text[0].text, "Цена: " + price[0].text, "Продавец: " + user[0].text + "Отзывы: " + reviews[0].text + user_info[0].text])
		lp_dota2.append(object_dota2)

	r_dota2help = requests.get("https://funpay.com/lots/502/")
	html_dota2help = BS(r_dota2help.content, 'html.parser')
	help_dota2 = []
	for el in html_dota2help.select(".tc-item"):
		text = el.select(".tc-desc > .tc-desc-text")
		price = el.select(".tc-price > div")
		user = el.select(".media-user-name")
		reviews = el.select(".media-user-reviews")
		user_info = el.select(".media-user-info")
		object_dota2 = []
		object_dota2.extend(["Описание: " + text[0].text, "Цена: " + price[0].text, "Продавец: " + user[0].text + "Отзывы: " + reviews[0].text + user_info[0].text])
		help_dota2.append(object_dota2)

	r_dota2uslugdota = requests.get("https://funpay.com/lots/503/")
	html_dota2uslugdota = BS(r_dota2uslugdota.content, 'html.parser')
	uslugdota_dota2 = []
	for el in html_dota2uslugdota.select(".tc-item"):
		text = el.select(".tc-desc > .tc-desc-text")
		price = el.select(".tc-price > div")
		user = el.select(".media-user-name")
		reviews = el.select(".media-user-reviews")
		user_info = el.select(".media-user-info")
		object_dota2 = []
		object_dota2.extend(["Описание: " + text[0].text, "Цена: " + price[0].text, "Продавец: " + user[0].text + "Отзывы: " + reviews[0].text + user_info[0].text])
		uslugdota_dota2.append(object_dota2)

	r_dota2kompend = requests.get("https://funpay.com/lots/661/")
	html_dota2kompend = BS(r_dota2kompend.content, 'html.parser')
	kompend_dota2 = []
	for el in html_dota2kompend.select(".tc-item"):
		text = el.select(".tc-desc > .tc-desc-text")
		price = el.select(".tc-price > div")
		user = el.select(".media-user-name")
		reviews = el.select(".media-user-reviews")
		user_info = el.select(".media-user-info")
		object_dota2 = []
		object_dota2.extend(["Описание: " + text[0].text, "Цена: " + price[0].text, "Продавец: " + user[0].text + "Отзывы: " + reviews[0].text + user_info[0].text])
		kompend_dota2.append(object_dota2)

	r_dota2more = requests.get("https://funpay.com/lots/504/")
	html_dota2more = BS(r_dota2more.content, 'html.parser')
	more_dota2 = []
	for el in html_dota2more.select(".tc-item"):
		text = el.select(".tc-desc > .tc-desc-text")
		price = el.select(".tc-price > div")
		user = el.select(".media-user-name")
		reviews = el.select(".media-user-reviews")
		user_info = el.select(".media-user-info")
		object_dota2 = []
		object_dota2.extend(["Описание: " + text[0].text, "Цена: " + price[0].text, "Продавец: " + user[0].text + "Отзывы: " + reviews[0].text + user_info[0].text])
		more_dota2.append(object_dota2)
	return more_dota2
print(dota2())