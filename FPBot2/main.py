import telebot, requests
from telebot import types
from bs4 import BeautifulSoup as BS
import time
bot = telebot.TeleBot('6605974541:AAHK8C1ZwDC4JpTNqfC-Fvxhm4ucCqJnbLo')

gamelist = ['ARK: Survival Evolved', 'Black Russia', 'Brawl Stars', 'CarX Drift Racing', 'Counter-Strike 2', 'Crossout', 'Cyberpunk 2077', 'Dead by Daylight', 'Dota 2', 'Dying Light 2', 'GTA5', 'Hearts of Iron IV', 'Minecraft', 'Mobile Legends', 'PUBG', 'PUBG Mobile', 'Radmir', 'Rust', 'War Thunder', 'Warface', 'World of Tanks', 'World of Tanks Blitz','YouTube', 'Telegram Premium', 'ВК', 'Netflix']

@bot.message_handler(commands=['start'])
def cmd_start(message):
    markup_re = types.ReplyKeyboardMarkup()
    button1 = types.KeyboardButton('Выбрать игру')
    markup_re.row(button1)
    bot.send_message(message.chat.id, 'Добро пожаловать в телеграмм бот - парсер игровой биржи <b>FunPay! Для большей информации - /help</b>', parse_mode='html', reply_markup=markup_re)
    bot.register_next_step_handler(message, on_click)

# @bot.message_handler(content_types='text')
# def on_click(message):
#     if message.text == 'Выбрать игру':
#         murkup_page1 = types.InlineKeyboardMarkup()
#         game8 = types.InlineKeyboardButton('Dota 2', callback_data='dota')
#         murkup_page1.row(game8)
#         bot.send_message(message.chat.id, '🎮Выберите игру из списка ниже!', reply_markup=murkup_page1)


@bot.message_handler(commands=['help'])
def cmd_help(message):
    bot.send_message(message.chat.id, '🦾Данный бот создан для парсинга <u>самых популярных игр</u> с биржи <b>FunPay</b>, здесь вы можете подобрать для себя самый лучший вариант какой либо услуги по цене/качеству🥇✔', parse_mode='html')

@bot.message_handler(content_types='text')
def on_click(message):
    if message.text == 'Выбрать игру':
        murkup_page1 = types.InlineKeyboardMarkup()
        game1 = types.InlineKeyboardButton('ARK', callback_data='ark')
        game2 = types.InlineKeyboardButton('Black Russia', callback_data='br')
        game4 = types.InlineKeyboardButton('CarX', callback_data='carx')
        game5 = types.InlineKeyboardButton('CS Go 2', callback_data='cs')
        game6 = types.InlineKeyboardButton('Crossout', callback_data='cr')
        nextp = types.InlineKeyboardButton('Следующая страница>>', callback_data='p2')
        murkup_page1.row(game1, game2)
        murkup_page1.row(game4)
        murkup_page1.row(game5, game6)
        murkup_page1.row(nextp)
        bot.send_message(message.chat.id, '🎮Выберите игру из списка ниже!', reply_markup=murkup_page1)


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'p1':
             murkup2_page1 = types.InlineKeyboardMarkup()
             game1 = types.InlineKeyboardButton('ARK', callback_data='ark')
             game2 = types.InlineKeyboardButton('Black Russia', callback_data='br')
             game4 = types.InlineKeyboardButton('CarX', callback_data='carx')
             game5 = types.InlineKeyboardButton('CS Go 2', callback_data='cs')
             game6 = types.InlineKeyboardButton('Crossout', callback_data='cr')
             nextp = types.InlineKeyboardButton('Следующая страница>>', callback_data='p2')
             murkup2_page1.row(game1, game2)
             murkup2_page1.row(game4)
             murkup2_page1.row(game5, game6)
             murkup2_page1.row(nextp)
             bot.send_message(callback.message.chat.id, '🎮Выберите игру из списка ниже!', reply_markup=murkup2_page1)

    elif callback.data == 'p2':
        murkup_2page = types.InlineKeyboardMarkup()
        game7 = types.InlineKeyboardButton('Dead by Daylight', callback_data='dbd')
        game8 = types.InlineKeyboardButton('Dota 2', callback_data='dota')
        game9 = types.InlineKeyboardButton('Dying Light 2', callback_data='dl')
        game10 = types.InlineKeyboardButton('GTA5 Online', callback_data='gta')
        game11 = types.InlineKeyboardButton('HoI IV', callback_data='hoi')
        game12 = types.InlineKeyboardButton('Minecraft', callback_data='mn')
        nextp2 = types.InlineKeyboardButton('Следующая страница>>', callback_data='p3')
        prevp = types.InlineKeyboardButton('<<Предыдущая страница', callback_data='p1')
        murkup_2page.row(game7, game8)
        murkup_2page.row(game9, game10)
        murkup_2page.row(game11, game12)
        murkup_2page.row(prevp, nextp2)
        bot.send_message(callback.message.chat.id, '🕹Выберите игру из списка ниже!  2 страница', reply_markup=murkup_2page)

    elif callback.data == 'p3':
        murkup_3page = types.InlineKeyboardMarkup()
        game13 = types.InlineKeyboardButton('Mobl', callback_data='mb')
        game14 = types.InlineKeyboardButton('PUBG', callback_data='pubg')
        game15 = types.InlineKeyboardButton('PUBG Mobile', callback_data='pubgm')
        game16 = types.InlineKeyboardButton('Radmir', callback_data='rr')
        game17 = types.InlineKeyboardButton('Rust', callback_data='ru')
        game18 = types.InlineKeyboardButton('War Thunder', callback_data='wt')
        nextp3 = types.InlineKeyboardButton('Следующая страница>>', callback_data='p4')
        prevp2 = types.InlineKeyboardButton('<<Предыдущая страница', callback_data='p2')
        murkup_3page.row(game13, game14)
        murkup_3page.row(game15, game16)
        murkup_3page.row(game17, game18)
        murkup_3page.row(prevp2, nextp3)
        bot.send_message(callback.message.chat.id, '🎲Выберите игру из списка ниже! 3 страница', reply_markup=murkup_3page)

    elif callback.data == 'p4':
        murkup_4page = types.InlineKeyboardMarkup()
        game19 = types.InlineKeyboardButton('Warface', callback_data='wf')
        game20 = types.InlineKeyboardButton('Wot', callback_data='wot')
        game21 = types.InlineKeyboardButton('WotB', callback_data='wotb')
        game22 = types.InlineKeyboardButton('YouTube', callback_data='yt')
        game23 = types.InlineKeyboardButton('Telegram', callback_data='tg')
        game24 = types.InlineKeyboardButton('VK', callback_data='vk')
        nextp4 = types.InlineKeyboardButton('Последняя страница>>', callback_data='p5')
        prevp3 = types.InlineKeyboardButton('<<Предыдущая страница', callback_data='p3')
        murkup_4page.row(game19, game20)
        murkup_4page.row(game21, game22)
        murkup_4page.row(game23, game24)
        murkup_4page.row(prevp3, nextp4)
        bot.send_message(callback.message.chat.id, '🎰Выберите игру из списка ниже! 4 страница', reply_markup=murkup_4page)

    elif callback.data == 'p5':
        murkup_5page = types.InlineKeyboardMarkup()
        game25 = types.InlineKeyboardButton('Netflix', callback_data='ns')
        prevp4 = types.InlineKeyboardButton('<<Предыдущая страница', callback_data='p4')
        murkup_5page.row(game25)
        murkup_5page.row(prevp4)
        bot.send_message(callback.message.chat.id, '🏀Выберите игру из списка ниже! 5 страница', reply_markup=murkup_5page)
    elif callback.data == 'ark':
        murkup_ark = types.InlineKeyboardMarkup()
        answery = types.InlineKeyboardButton('Да', callback_data='y1')
        answern = types.InlineKeyboardButton('Нет', callback_data='no')
        murkup_ark.row(answery, answern)
        bot.send_message(callback.message.chat.id, 'Начать ли отслеживать объявления?', reply_markup=murkup_ark)
    elif callback.data == 'y1':
        backark_offer = 0
        while True:
            offerark_text = parserark(backark_offer)
            backark_offer = offerark_text[1]
            if offerark_text[0] != None:
                bot.send_message(callback.message.chat.id, offerark_text)
                time.sleep(600)
    elif callback.data == 'br':
        murkup_br = types.InlineKeyboardMarkup()
        ybr = types.InlineKeyboardButton('Да', callback_data='y2')
        nbr = types.InlineKeyboardButton('Нет', callback_data='no')
        murkup_br.row(ybr, nbr)
        bot.send_message(callback.message.chat.id, 'Начать ли отслеживать объявления?', reply_markup=murkup_br)
    elif callback.data == 'y2':
        backbr_offer = 0
        while True:
            offerbr_text = parserbr(backbr_offer)
            backbr_offer = offerbr_text[1]
            if offerbr_text[0] != None:
                bot.send_message(callback.message.chat.id, offerbr_text)
                time.sleep(600)
    elif callback.data == 'carx':
        murkup_carx = types.InlineKeyboardMarkup()
        ycarx = types.InlineKeyboardButton('Да', callback_data='y3')
        ncarx = types.InlineKeyboardButton('Нет', callback_data='no')
        murkup_carx.row(ycarx, ncarx)
        bot.send_message(callback.message.chat.id, 'Начать ли отслеживать объявления?', reply_markup=murkup_carx)
    elif callback.data == 'y3':
        backcarx_offer = 0
        while True:
            offercarx_text = parsercarx(backcarx_offer)
            backcarx_offer = offercarx_text[1]
            if offercarx_text[0] != None:
                bot.send_message(callback.message.chat.id, offercarx_text)
                time.sleep(600)
    elif callback.data == 'cs':
        murkup_cs = types.InlineKeyboardMarkup()
        ycs = types.InlineKeyboardButton('Да', callback_data='y4')
        ncs = types.InlineKeyboardButton('Нет', callback_data='no')
        murkup_cs.row(ycs, ncs)
        bot.send_message(callback.message.chat.id, 'Начать ли отслеживать объявления?', reply_markup=murkup_cs)
    elif callback.data == 'y4':
        backcs_offer = 0
        while True:
            offercs_text = parsercs(backcs_offer)
            backcs_offer = offercs_text[1]
            if offercs_text[0] != None:
                bot.send_message(callback.message.chat.id, offercs_text)
                time.sleep(600)
    elif callback.data == 'cr':
        murkup_cr = types.InlineKeyboardMarkup()
        ycr = types.InlineKeyboardButton('Да', callback_data='y5')
        ncr = types.InlineKeyboardButton('Нет', callback_data='no')
        murkup_cr.row(ycr, ncr)
        bot.send_message(callback.message.chat.id, 'Начать ли отслеживать объявления?', reply_markup=murkup_cr)
    elif callback.data == 'y5':
        backcr_offer = 0
        while True:
            offercr_text = parsercr(backcr_offer)
            backcr_offer = offercr_text[1]
            if offercr_text[0] != None:
                bot.send_message(callback.message.chat.id, offercr_text)
                time.sleep(600)
    elif callback.data == 'dbd':
        murkup_dbd = types.InlineKeyboardMarkup()
        ydbd = types.InlineKeyboardButton('Да', callback_data='y6')
        ndbd = types.InlineKeyboardButton('Нет', callback_data='no')
        murkup_dbd.row(ydbd, ndbd)
        bot.send_message(callback.message.chat.id, 'Начать ли отслеживать объявления?', reply_markup=murkup_dbd)
    elif callback.data == 'y6':
        backdbd_offer = 0
        while True:
            offerdbd_text = parserdbd(backdbd_offer)
            backdbd_offer = offerdbd_text[1]
            if offerdbd_text[0] != None:
                bot.send_message(callback.message.chat.id, offerdbd_text)
                time.sleep(600)
    elif callback.data == 'dota':
        murkup_dota = types.InlineKeyboardMarkup()
        answery = types.InlineKeyboardButton('Да', callback_data='y')
        answern = types.InlineKeyboardButton('Нет', callback_data='no')
        murkup_dota.row(answery, answern)
        bot.send_message(callback.message.chat.id, 'Начать ли отслеживать объявления?', reply_markup=murkup_dota)
    elif callback.data == 'y':
        back_offer = 0
        while True:
            offer_text = parserdota(back_offer)
            back_offer = offer_text[1]
            if offer_text[0] != None:
                bot.send_message(callback.message.chat.id, offer_text)
                time.sleep(600)
    elif callback.data == 'dl':
        murkup_dl = types.InlineKeyboardMarkup()
        ydl = types.InlineKeyboardButton('Да', callback_data='y7')
        ndl = types.InlineKeyboardButton('Нет', callback_data='no')
        murkup_dl.row(ydl, ndl)
        bot.send_message(callback.message.chat.id, 'Начать ли отслеживать объявления?', reply_markup=murkup_dl)
    elif callback.data == 'y7':
        backdl_offer = 0
        while True:
            offerdl_text = parserdl(backdl_offer)
            backdl_offer = offerdl_text[1]
            if offerdl_text[0] != None:
                bot.send_message(callback.message.chat.id, offerdl_text)
                time.sleep(600)
    elif callback.data == 'gta':
        murkup_gta = types.InlineKeyboardMarkup()
        ygta = types.InlineKeyboardButton('Да', callback_data='y8')
        ngta = types.InlineKeyboardButton('Нет', callback_data='no')
        murkup_gta.row(ygta, ngta)
        bot.send_message(callback.message.chat.id, 'Начать ли отслеживать объявления?', reply_markup=murkup_gta)
    elif callback.data == 'y8':
        backgta_offer = 0
        while True:
            offergta_text = parsergta(backgta_offer)
            backgta_offer = offergta_text[1]
            if offergta_text[0] != None:
                bot.send_message(callback.message.chat.id, offergta_text)
                time.sleep(600)
    elif callback.data == 'hoi':
        murkup_hoi = types.InlineKeyboardMarkup()
        yhoi = types.InlineKeyboardButton('Да', callback_data='y9')
        nhoi = types.InlineKeyboardButton('Нет', callback_data='no')
        murkup_hoi.row(yhoi, nhoi)
        bot.send_message(callback.message.chat.id, 'Начать ли отслеживать объявления?', reply_markup=murkup_hoi)
    elif callback.data == 'y9':
        backhoi_offer = 0
        while True:
            offerhoi_text = parserhoi(backhoi_offer)
            backhoi_offer = offerhoi_text[1]
            if offerhoi_text[0] != None:
                bot.send_message(callback.message.chat.id, offerhoi_text)
                time.sleep(600)
    elif callback.data == 'mn':
        murkup_mn = types.InlineKeyboardMarkup()
        ymn = types.InlineKeyboardButton('Да', callback_data='y10')
        nmn = types.InlineKeyboardButton('Нет', callback_data='no')
        murkup_mn.row(ymn, nmn)
        bot.send_message(callback.message.chat.id, 'Начать ли отслеживать объявления?', reply_markup=murkup_mn)
    elif callback.data == 'y10':
        backmn_offer = 0
        while True:
            offermn_text = parsermn(backmn_offer)
            backmn_offer = offermn_text[1]
            if offermn_text[0] != None:
                bot.send_message(callback.message.chat.id, offermn_text)
                time.sleep(600)
    elif callback.data == 'mb':
        murkup_mb = types.InlineKeyboardMarkup()
        ymb = types.InlineKeyboardButton('Да', callback_data='y11')
        nmb = types.InlineKeyboardButton('Нет', callback_data='no')
        murkup_mb.row(ymb, nmb)
        bot.send_message(callback.message.chat.id, 'Начать ли отслеживать объявления?', reply_markup=murkup_mb)
    elif callback.data == 'y11':
        backmb_offer = 0
        while True:
            offermb_text = parsermb(backmb_offer)
            backmb_offer = offermb_text[1]
            if offermb_text[0] != None:
                bot.send_message(callback.message.chat.id, offermb_text)
                time.sleep(600)
    elif callback.data == 'pubg':
        murkup_pubg = types.InlineKeyboardMarkup()
        ypubg = types.InlineKeyboardButton('Да', callback_data='y12')
        npubg = types.InlineKeyboardButton('Нет', callback_data='no')
        murkup_pubg.row(ypubg, npubg)
        bot.send_message(callback.message.chat.id, 'Начать ли отслеживать объявления?', reply_markup=murkup_pubg)
    elif callback.data == 'y12':
        backpubg_offer = 0
        while True:
            offerpubg_text = parserpubg(backpubg_offer)
            backpubg_offer = offerpubg_text[1]
            if offerpubg_text[0] != None:
                bot.send_message(callback.message.chat.id, offerpubg_text)
                time.sleep(600)
    elif callback.data == 'pubgm':
        murkup_pubgm = types.InlineKeyboardMarkup()
        ypubgm = types.InlineKeyboardButton('Да', callback_data='y13')
        npubgm = types.InlineKeyboardButton('Нет', callback_data='no')
        murkup_pubgm.row(ypubgm, npubgm)
        bot.send_message(callback.message.chat.id, 'Начать ли отслеживать объявления?', reply_markup=murkup_pubgm)
    elif callback.data == 'y13':
        backpubgm_offer = 0
        while True:
            offerpubgm_text = parserpubg(backpubgm_offer)
            backpubgm_offer = offerpubgm_text[1]
            if offerpubgm_text[0] != None:
                bot.send_message(callback.message.chat.id, offerpubgm_text)
                time.sleep(600)
def parserdota(back_offer):
    r_dota2acc = requests.get("https://funpay.com/lots/81/")
    html_dota2acc = BS(r_dota2acc.content, 'html.parser')
    offer = html_dota2acc.find("a", class_="tc-item")
    if offer != back_offer:
        title = offer.find("div", class_="tc-desc-text").text.strip()
        user = offer.find("div", class_="media-user-name").text.strip()
        price = offer.find("div", class_="tc-price").text.strip()
        url = html_dota2acc.find("a", class_="tc-item offer-promo", href=True)["href"].strip()
        print(title, user, price, url, sep="\n\n")
        return f'{title}\n{user}\n{price}\n{url}'
    else:
        return None, offer
def parserark(backark_offer):
    r_arkacc = requests.get("https://funpay.com/lots/327/")
    html_arkacc = BS(r_arkacc.content, 'html.parser')
    offer = html_arkacc.find("a", class_="tc-item")
    if offer != backark_offer:
        title = offer.find("div", class_="tc-desc-text").text.strip()
        user = offer.find("div", class_="media-user-name").text.strip()
        price = offer.find("div", class_="tc-price").text.strip()
        url = html_arkacc.find("a", class_= "tc-item", href=True)["href"].strip()
        print(title, user, price, url, sep="\n\n")
        return f'{title}\n{user}\n{price}\n{url}'
    else:
        return None, offer
def parserbr(backbr_offer):
    r_bracc = requests.get("https://funpay.com/lots/1442/")
    html_bracc = BS(r_bracc.content, 'html.parser')
    offer = html_bracc.find("a", class_="tc-item")
    if offer != backbr_offer:
        title = offer.find("div", class_="tc-desc-text").text.strip()
        user = offer.find("div", class_="media-user-name").text.strip()
        price = offer.find("div", class_="tc-price").text.strip()
        url = html_bracc.find("a", class_= "tc-item", href=True)["href"].strip()
        print(title, user, price, url, sep="\n\n")
        return f'{title}\n{user}\n{price}\n{url}'
    else:
        return None, offer
def parsercarx(backcarx_offer):
    r_carxacc = requests.get("https://funpay.com/lots/902/")
    html_carxacc = BS(r_carxacc.content, 'html.parser')
    offer = html_carxacc.find("a", class_="tc-item")
    if offer != backcarx_offer:
        title = offer.find("div", class_="tc-desc-text").text.strip()
        user = offer.find("div", class_="media-user-name").text.strip()
        price = offer.find("div", class_="tc-price").text.strip()
        url = html_carxacc.find("a", class_= "tc-item", href=True)["href"].strip()
        print(title, user, price, url, sep="\n\n")
        return f'{title}\n{user}\n{price}\n{url}'
    else:
        return None, offer
def parsercs(backcs_offer):
    r_csacc = requests.get("https://funpay.com/lots/1350/")
    html_csacc = BS(r_csacc.content, 'html.parser')
    offer = html_csacc.find("a", class_="tc-item")
    if offer != backcs_offer:
        title = offer.find("div", class_="tc-desc-text").text.strip()
        user = offer.find("div", class_="media-user-name").text.strip()
        price = offer.find("div", class_="tc-price").text.strip()
        url = html_csacc.find("a", class_= "tc-item", href=True)["href"].strip()
        print(title, user, price, url, sep="\n\n")
        return f'{title}\n{user}\n{price}\n{url}'
    else:
        return None, offer
def parsercr(backcr_offer):
    r_cracc = requests.get("https://funpay.com/lots/212/")
    html_cracc = BS(r_cracc.content, 'html.parser')
    offer = html_cracc.find("a", class_="tc-item")
    if offer != backcr_offer:
        title = offer.find("div", class_="tc-desc-text").text.strip()
        user = offer.find("div", class_="media-user-name").text.strip()
        price = offer.find("div", class_="tc-price").text.strip()
        url = html_cracc.find("a", class_= "tc-item", href=True)["href"].strip()
        print(title, user, price, url, sep="\n\n")
        return f'{title}\n{user}\n{price}\n{url}'
    else:
        return None, offer
def parserdbd(backdbd_offer):
    r_dbdacc = requests.get("https://funpay.com/lots/460/")
    html_dbdacc = BS(r_dbdacc.content, 'html.parser')
    offer = html_dbdacc.find("a", class_="tc-item")
    if offer != backdbd_offer:
        title = offer.find("div", class_="tc-desc-text").text.strip()
        user = offer.find("div", class_="media-user-name").text.strip()
        price = offer.find("div", class_="tc-price").text.strip()
        url = html_dbdacc.find("a", class_= "tc-item", href=True)["href"].strip()
        print(title, user, price, url, sep="\n\n")
        return f'{title}\n{user}\n{price}\n{url}'
    else:
        return None, offer
def parserdl(backdl_offer):
    r_dlacc = requests.get("https://funpay.com/lots/868/")
    html_dlacc = BS(r_dlacc.content, 'html.parser')
    offer = html_dlacc.find("a", class_="tc-item")
    if offer != backdl_offer:
        title = offer.find("div", class_="tc-desc-text").text.strip()
        user = offer.find("div", class_="media-user-name").text.strip()
        price = offer.find("div", class_="tc-price").text.strip()
        url = html_dlacc.find("a", class_= "tc-item", href=True)["href"].strip()
        print(title, user, price, url, sep="\n\n")
        return f'{title}\n{user}\n{price}\n{url}'
    else:
        return None, offer
def parsergta(backgta_offer):
    r_gtaacc = requests.get("https://funpay.com/lots/87/")
    html_gtaacc = BS(r_gtaacc.content, 'html.parser')
    offer = html_gtaacc.find("a", class_="tc-item")
    if offer != backgta_offer:
        title = offer.find("div", class_="tc-desc-text").text.strip()
        user = offer.find("div", class_="media-user-name").text.strip()
        price = offer.find("div", class_="tc-price").text.strip()
        url = html_gtaacc.find("a", class_= "tc-item", href=True)["href"].strip()
        print(title, user, price, url, sep="\n\n")
        return f'{title}\n{user}\n{price}\n{url}'
    else:
        return None, offer
def parserhoi(backhoi_offer):
    r_hoiacc = requests.get("https://funpay.com/lots/1710/")
    html_hoiacc = BS(r_hoiacc.content, 'html.parser')
    offer = html_hoiacc.find("a", class_="tc-item")
    if offer != backhoi_offer:
        title = offer.find("div", class_="tc-desc-text").text.strip()
        user = offer.find("div", class_="media-user-name").text.strip()
        price = offer.find("div", class_="tc-price").text.strip()
        url = html_hoiacc.find("a", class_= "tc-item", href=True)["href"].strip()
        print(title, user, price, url, sep="\n\n")
        return f'{title}\n{user}\n{price}\n{url}'
    else:
        return None, offer
def parsermn(backmn_offer):
    r_mnacc = requests.get("https://funpay.com/lots/221/")
    html_mnacc = BS(r_mnacc.content, 'html.parser')
    offer = html_mnacc.find("a", class_="tc-item")
    if offer != backmn_offer:
        title = offer.find("div", class_="tc-desc-text").text.strip()
        user = offer.find("div", class_="media-user-name").text.strip()
        price = offer.find("div", class_="tc-price").text.strip()
        url = html_mnacc.find("a", class_= "tc-item", href=True)["href"].strip()
        print(title, user, price, url, sep="\n\n")
        return f'{title}\n{user}\n{price}\n{url}'
    else:
        return None, offer
def parsermb(backmb_offer):
    r_mbacc = requests.get("https://funpay.com/lots/366/")
    html_mbacc = BS(r_mbacc.content, 'html.parser')
    offer = html_mbacc.find("a", class_="tc-item")
    if offer != backmb_offer:
        title = offer.find("div", class_="tc-desc-text").text.strip()
        user = offer.find("div", class_="media-user-name").text.strip()
        price = offer.find("div", class_="tc-price").text.strip()
        url = html_mbacc.find("a", class_= "tc-item", href=True)["href"].strip()
        print(title, user, price, url, sep="\n\n")
        return f'{title}\n{user}\n{price}\n{url}'
    else:
        return None, offer
def parserpubg(backpubg_offer):
    r_pubgacc = requests.get("https://funpay.com/lots/215/")
    html_pubgacc = BS(r_pubgacc.content, 'html.parser')
    offer = html_pubgacc.find("a", class_="tc-item")
    if offer != backpubg_offer:
        title = offer.find("div", class_="tc-desc-text").text.strip()
        user = offer.find("div", class_="media-user-name").text.strip()
        price = offer.find("div", class_="tc-price").text.strip()
        url = html_pubgacc.find("a", class_= "tc-item", href=True)["href"].strip()
        print(title, user, price, url, sep="\n\n")
        return f'{title}\n{user}\n{price}\n{url}'
    else:
        return None, offer
def parserpubgm(backpubgm_offer):
    r_pubgmacc = requests.get("https://funpay.com/lots/346/")
    html_pubgmacc = BS(r_pubgmacc.content, 'html.parser')
    offer = html_pubgmacc.find("a", class_="tc-item")
    if offer != backpubgm_offer:
        title = offer.find("div", class_="tc-desc-text").text.strip()
        user = offer.find("div", class_="media-user-name").text.strip()
        price = offer.find("div", class_="tc-price").text.strip()
        url = html_pubgmacc.find("a", class_= "tc-item", href=True)["href"].strip()
        print(title, user, price, url, sep="\n\n")
        return f'{title}\n{user}\n{price}\n{url}'
    else:
        return None, offer
#     elif callback.data == 'rr':
#         murkup_rr = types.InlineKeyboardMarkup()
#         category1_rr = types.InlineKeyboardButton('Вирты💵', callback_data='virts15')
#         category2_rr = types.InlineKeyboardButton('Аккаунты📑', callback_data='acc15')
#         category3_rr = types.InlineKeyboardButton('Донат💲', callback_data='donat15')
#         category4_rr = types.InlineKeyboardButton('Предметы🎲', callback_data='predm15')
#         category5_rr = types.InlineKeyboardButton('Услуги✔', callback_data='uslug15')
#         category6_rr = types.InlineKeyboardButton('Прочее▶', callback_data='more15')
#         murkup_rr.row(category1_rr, category2_rr)
#         murkup_rr.row(category3_rr, category4_rr)
#         murkup_rr.row(category5_rr, category6_rr)
#         bot.send_message(callback.message.chat.id, 'Хороший выбор!👍 Теперь выберите категорию📝', reply_markup=murkup_rr)
#     elif callback.data == 'ru':
#         murkup_ru = types.InlineKeyboardMarkup()
#         category1_ru = types.InlineKeyboardButton('Аккаунты📑', callback_data='acc16')
#         category2_ru = types.InlineKeyboardButton('Ключи🗝', callback_data='keys16')
#         category3_ru = types.InlineKeyboardButton('Монеты', callback_data='money16')
#         category4_ru = types.InlineKeyboardButton('Предметы🎲', callback_data='predm16')
#         category5_ru = types.InlineKeyboardButton('Услуги✔', callback_data='uslug16')
#         category6_ru = types.InlineKeyboardButton('VIP пропуск💎', callback_data='vip16')
#         category7_ru = types.InlineKeyboardButton('Twitch Drops', callback_data='twitch16')
#         category8_ru = types.InlineKeyboardButton('Прочее▶', callback_data='more16')
#         murkup_ru.row(category1_ru, category2_ru)
#         murkup_ru.row(category3_ru, category4_ru)
#         murkup_ru.row(category5_ru, category6_ru)
#         murkup_ru.row(category7_ru, category8_ru)
#         bot.send_message(callback.message.chat.id, 'Хороший выбор!👍 Теперь выберите категорию📝', reply_markup=murkup_ru)
#     elif callback.data == 'wt':
#         murkup_wt = types.InlineKeyboardMarkup()
#         category1_wt = types.InlineKeyboardButton('Фарм серебра💵', callback_data='money17')
#         category2_wt = types.InlineKeyboardButton('Аккаунты📑', callback_data='acc17')
#         category3_wt = types.InlineKeyboardButton('Прокачка📈', callback_data='boost17')
#         category4_wt = types.InlineKeyboardButton('Бонус-коды', callback_data='bonus17')
#         category5_wt = types.InlineKeyboardButton('Прочее▶', callback_data='more17')
#         murkup_wt.row(category2_wt, category1_wt)
#         murkup_wt.row(category3_wt, category4_wt)
#         murkup_wt.row(category5_wt)
#         bot.send_message(callback.message.chat.id, 'Хороший выбор!👍 Теперь выберите категорию📝', reply_markup=murkup_wt)
#     elif callback.data == 'wf':
#         murkup_wf = types.InlineKeyboardMarkup()
#         category1_wf = types.InlineKeyboardButton('Аккаунты📑', callback_data='acc18')
#         category3_wf = types.InlineKeyboardButton('Буст PM📈', callback_data='boost118')
#         category2_wf = types.InlineKeyboardButton('Предметы🎲', callback_data='predm18')
#         category4_wf = types.InlineKeyboardButton('Буст спецопераций📈', callback_data='boost218')
#         category5_wf = types.InlineKeyboardButton('Буст побед📈', callback_data='boost318')
#         category6_wf = types.InlineKeyboardButton('Буст статистики📈', callback_data='boost418')
#         category7_wf = types.InlineKeyboardButton('Кредиты💵', callback_data='money18')
#         np_wf = types.InlineKeyboardButton('Следующая страница>>', callback_data='npc4')
#         murkup_wf.row(category1_wf, category2_wf)
#         murkup_wf.row(category3_wf, category4_wf)
#         murkup_wf.row(category5_wf, category6_wf)
#         murkup_wf.row(category7_wf, np_wf)
#         bot.send_message(callback.message.chat.id, 'Хороший выбор!👍 Теперь выберите категорию📝', reply_markup=murkup_wf)
#     elif callback.data == 'wot':
#         murkup_wot = types.InlineKeyboardMarkup()
#         category1_wot = types.InlineKeyboardButton('Аккаунты📑', callback_data='acc19')
#         category2_wot = types.InlineKeyboardButton('Бонус-коды', callback_data='bonus19')
#         category3_wot = types.InlineKeyboardButton('Буст📈', callback_data='boost19')
#         category4_wot = types.InlineKeyboardButton('Фарм серебра💵', callback_data='money19')
#         category5_wot = types.InlineKeyboardButton('Выполнение ЛБЗ', callback_data='lbz19')
#         category6_wot = types.InlineKeyboardButton('Обучение🤓', callback_data='help19')
#         category7_wot = types.InlineKeyboardButton('Донат💲', callback_data='donat19')
#         np_wot = types.InlineKeyboardButton('Следующая страница>>', callback_data='npc5')
#         murkup_wot.row(category1_wot, category2_wot)
#         murkup_wot.row(category3_wot, category4_wot)
#         murkup_wot.row(category5_wot, category6_wot)
#         murkup_wot.row(category7_wot, np_wot)
#         bot.send_message(callback.message.chat.id, 'Хороший выбор!👍 Теперь выберите категорию📝', reply_markup=murkup_wot)
#     elif callback.data == 'wotb':
#         murkup_wotb = types.InlineKeyboardMarkup()
#         category1_wotb = types.InlineKeyboardButton('Аккаунты📑', callback_data='acc20')
#         category2_wotb = types.InlineKeyboardButton('Буст📈', callback_data='boost20')
#         category3_wotb = types.InlineKeyboardButton('Фарм серебра💵', callback_data='money20')
#         category4_wotb = types.InlineKeyboardButton('Обучение🤓', callback_data='help20')
#         category5_wotb = types.InlineKeyboardButton('Золото💰', callback_data='gold20')
#         category6_wotb = types.InlineKeyboardButton('Донат💲', callback_data='donat20')
#         category7_wotb = types.InlineKeyboardButton('Бонус-коды', callback_data='bonus20')
#         category9_wotb = types.InlineKeyboardButton('Прочее▶', callback_data='more20')
#         category8_wotb = types.InlineKeyboardButton('Кланы👨‍💻', callback_data='clan20')
#         murkup_wotb.row(category1_wotb, category2_wotb)
#         murkup_wotb.row(category3_wotb, category4_wotb)
#         murkup_wotb.row(category5_wotb, category6_wotb)
#         murkup_wotb.row(category7_wotb, category8_wotb)
#         murkup_wotb.row(category9_wotb)
#         bot.send_message(callback.message.chat.id, 'Хороший выбор!👍 Теперь выберите категорию📝', reply_markup=murkup_wotb)
#     elif callback.data == 'yt':
#         murkup_yt = types.InlineKeyboardMarkup()
#         category1_yt = types.InlineKeyboardButton('Услуги✔', callback_data='uslug21')
#         category2_yt = types.InlineKeyboardButton('Канал', callback_data='chan21')
#         category3_yt = types.InlineKeyboardButton('Premium💎', callback_data='prime21')
#         murkup_yt.row(category1_yt, category2_yt)
#         murkup_yt.row(category3_yt)
#         bot.send_message(callback.message.chat.id, 'Хороший выбор!👍 Теперь выберите категорию📝', reply_markup=murkup_yt)
#     elif callback.data == 'tg':
#         murkup_tg = types.InlineKeyboardMarkup()
#         category1_tg = types.InlineKeyboardButton('Каналы', callback_data='chan22')
#         category2_tg = types.InlineKeyboardButton('Услуги✔', callback_data='uslug22')
#         category3_tg = types.InlineKeyboardButton('Premium💎', callback_data='prime22')
#         category4_tg = types.InlineKeyboardButton('Прочее▶', callback_data='more22')
#         murkup_tg.row(category1_tg, category2_tg)
#         murkup_tg.row(category3_tg, category4_tg)
#         bot.send_message(callback.message.chat.id, 'Хороший выбор!👍 Теперь выберите категорию📝', reply_markup=murkup_tg)
#     elif callback.data == 'vk':
#         murkup_vk = types.InlineKeyboardMarkup()
#         category1_vk = types.InlineKeyboardButton('Услуги✔', callback_data='uslug23')
#         category2_vk = types.InlineKeyboardButton('Сообщества', callback_data='chan23')
#         murkup_vk.row(category1_vk, category2_vk)
#         bot.send_message(callback.message.chat.id, 'Хороший выбор!👍 Теперь выберите категорию📝', reply_markup=murkup_vk)
#     elif callback.data == 'ns':
#         murkup_ns = types.InlineKeyboardMarkup()
#         category1_ns = types.InlineKeyboardButton('Аккаунты📑', callback_data='acc24')
#         category2_ns = types.InlineKeyboardButton('Подписка', callback_data='sub24')
#         category3_ns = types.InlineKeyboardButton('Подарочные карты', callback_data='card24')
#         murkup_ns.row(category1_ns, category2_ns)
#         murkup_ns.row(category3_ns)
#         bot.send_message(callback.message.chat.id, 'Хороший выбор!👍 Теперь выберите категорию📝', reply_markup=murkup_ns)
#     elif callback.data == 'npc1':
#         murkup_dota2 = types.InlineKeyboardMarkup()
#         category8_dota = types.InlineKeyboardButton('Услуги Dota+💎', callback_data='uslugdota')
#         category9_dota = types.InlineKeyboardButton('Компендиум', callback_data='kompend')
#         category10_dota = types.InlineKeyboardButton('Прочее▶', callback_data='more7')
#         pp_dota = types.InlineKeyboardButton('<<Предыдущая страница', callback_data='dota')
#         murkup_dota2.row(category8_dota, category9_dota)
#         murkup_dota2.row(category10_dota, pp_dota)
#         bot.send_message(callback.message.chat.id, '2 страница категорий', reply_markup=murkup_dota2)
#     elif callback.data == 'npc2':
#         murkup_mn2 = types.InlineKeyboardMarkup()
#         category8_mn2 = types.InlineKeyboardButton('Game pass', callback_data='pass11')
#         category9_mn2 = types.InlineKeyboardButton('Конфиги', callback_data='conf11')
#         category10_mn2 = types.InlineKeyboardButton('Гайды', callback_data='guide11')
#         category11_mn2 = types.InlineKeyboardButton('Оффлайн активации', callback_data='offline11')
#         category12_mn2 = types.InlineKeyboardButton('Прочее▶', callback_data='more11')
#         pp_mn2 = types.InlineKeyboardButton('<<Предыдущая страница', callback_data='mn')
#         murkup_mn2.row(category8_mn2, category9_mn2)
#         murkup_mn2.row(category10_mn2, category11_mn2)
#         murkup_mn2.row(category12_mn2, pp_mn2)
#         bot.send_message(callback.message.chat.id, '2 страница категорий', reply_markup=murkup_mn2)
#     elif callback.data == 'npc3':
#         murkup_pubgm2 = types.InlineKeyboardMarkup()
#         category8_pubgm2 = types.InlineKeyboardButton('Популярность', callback_data='pop14')
#         category9_pubgm2 = types.InlineKeyboardButton('Прочее▶', callback_data='more14')
#         pp_pubgm2 = types.InlineKeyboardButton('<<Предыдущая страница', callback_data='pubgm')
#         murkup_pubgm2.row(category8_pubgm2, category9_pubgm2)
#         murkup_pubgm2.row(pp_pubgm2)
#         bot.send_message(callback.message.chat.id, '2 страница категорий', reply_markup=murkup_pubgm2)
#     elif callback.data == 'npc4':
#         murkup_wf2 = types.InlineKeyboardMarkup()
#         category8_wf2 = types.InlineKeyboardButton('Достижения', callback_data='dost18')
#         category9_wf2 = types.InlineKeyboardButton('Twitch Drops', callback_data='twitch18')
#         category10_wf2 = types.InlineKeyboardButton('Прочее▶', callback_data='more18')
#         pp_wf2 = types.InlineKeyboardButton('<<Предыдущая страница', callback_data='wf')
#         murkup_wf2.row(category8_wf2, category9_wf2)
#         murkup_wf2.row(category10_wf2, pp_wf2)
#         bot.send_message(callback.message.chat.id, '2 страница категорий', reply_markup=murkup_wf2)
#     elif callback.data == 'npc5':
#         murkup_wot2 = types.InlineKeyboardMarkup()
#         category8_wot2 = types.InlineKeyboardButton('Золото💰', callback_data='gold19')
#         category9_wot2 = types.InlineKeyboardButton('Кланы👨‍💻', callback_data='clans19')
#         category10_wot2 = types.InlineKeyboardButton('Коробки🎁', callback_data='box19')
#         category11_wot2 = types.InlineKeyboardButton('Prime Gaming💎', callback_data='prime19')
#         category12_wot2 = types.InlineKeyboardButton('Twitch Drops', callback_data='twitch19')
#         category13_wot2 = types.InlineKeyboardButton('Прочее▶', callback_data='more19')
#         pp_wot2 = types.InlineKeyboardButton('<<Предыдущая страница', callback_data='wot')
#         murkup_wot2.row(category8_wot2, category9_wot2)
#         murkup_wot2.row(category10_wot2, category11_wot2)
#         murkup_wot2.row(category12_wot2, category13_wot2)
#         murkup_wot2.row(pp_wot2)
#         bot.send_message(callback.message.chat.id, '2 страница категорий', reply_markup=murkup_wot2)


bot.polling(none_stop=True)