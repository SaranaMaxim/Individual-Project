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
    bot.send_message(message.chat.id, 'Добро пожаловать - 🦾Данный бот создан для парсинга <u>самых популярных игр</u> с биржи <b>FunPay</b>, здесь вы можете подобрать для себя самый лучший вариант какой либо услуги по цене/качеству🥇✔', parse_mode='html', reply_markup=markup_re)
    bot.register_next_step_handler(message, on_click)

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
    if callback.data == 'p1' or callback.data == "no":
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
        backark_postid = 0
        while True:
            offerark_text = parserark(backark_postid)
            backark_postid = offerark_text[1]
            print(offerark_text[1])
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
    elif callback.data == 'rr':
        murkup_rr = types.InlineKeyboardMarkup()
        yrr = types.InlineKeyboardButton('Да', callback_data='y14')
        nrr = types.InlineKeyboardButton('Нет', callback_data='no')
        murkup_rr.row(yrr, nrr)
        bot.send_message(callback.message.chat.id, 'Начать ли отслеживать объявления?', reply_markup=murkup_rr)
    elif callback.data == 'y14':
        backrr_offer = 0
        while True:
            offerrr_text = parserrr(backrr_offer)
            backrr_offer = offerrr_text[1]
            if offerrr_text[0] != None:
                bot.send_message(callback.message.chat.id, offerrr_text)
                time.sleep(600)
    elif callback.data == 'ru':
        murkup_ru = types.InlineKeyboardMarkup()
        yru = types.InlineKeyboardButton('Да', callback_data='y15')
        nru = types.InlineKeyboardButton('Нет', callback_data='no')
        murkup_ru.row(yru, nru)
        bot.send_message(callback.message.chat.id, 'Начать ли отслеживать объявления?', reply_markup=murkup_ru)
    elif callback.data == 'y15':
        backru_offer = 0
        while True:
            offerru_text = parserru(backru_offer)
            backru_offer = offerru_text[1]
            if offerru_text[0] != None:
                bot.send_message(callback.message.chat.id, offerru_text)
                time.sleep(600)
    elif callback.data == 'wt':
        murkup_wt = types.InlineKeyboardMarkup()
        ywt = types.InlineKeyboardButton('Да', callback_data='y16')
        nwt = types.InlineKeyboardButton('Нет', callback_data='no')
        murkup_wt.row(ywt, nwt)
        bot.send_message(callback.message.chat.id, 'Начать ли отслеживать объявления?', reply_markup=murkup_wt)
    elif callback.data == 'y16':
        backwt_offer = 0
        while True:
            offerwt_text = parserwt(backwt_offer)
            backwt_offer = offerwt_text[1]
            if offerwt_text[0] != None:
                bot.send_message(callback.message.chat.id, offerwt_text)
                time.sleep(600)
    elif callback.data == 'wf':
        murkup_wf = types.InlineKeyboardMarkup()
        ywf = types.InlineKeyboardButton('Да', callback_data='y17')
        nwf = types.InlineKeyboardButton('Нет', callback_data='no')
        murkup_wf.row(ywf, nwf)
        bot.send_message(callback.message.chat.id, 'Начать ли отслеживать объявления?', reply_markup=murkup_wf)
    elif callback.data == 'y17':
        backwf_offer = 0
        while True:
            offerwf_text = parserwf(backwf_offer)
            backwf_offer = offerwf_text[1]
            if offerwf_text[0] != None:
                bot.send_message(callback.message.chat.id, offerwf_text)
                time.sleep(600)
    elif callback.data == 'wot':
        murkup_wot = types.InlineKeyboardMarkup()
        ywot= types.InlineKeyboardButton('Да', callback_data='y18')
        nwot = types.InlineKeyboardButton('Нет', callback_data='no')
        murkup_wot.row(ywot, nwot)
        bot.send_message(callback.message.chat.id, 'Начать ли отслеживать объявления?', reply_markup=murkup_wot)
    elif callback.data == 'y18':
        backwot_offer = 0
        while True:
            offerwot_text = parserwot(backwot_offer)
            backwot_offer = offerwot_text[1]
            if offerwot_text[0] != None:
                bot.send_message(callback.message.chat.id, offerwot_text)
                time.sleep(600)
    elif callback.data == 'wotb':
        murkup_wotb = types.InlineKeyboardMarkup()
        ywotb = types.InlineKeyboardButton('Да', callback_data='y19')
        nwotb = types.InlineKeyboardButton('Нет', callback_data='no')
        murkup_wotb.row(ywotb, nwotb)
        bot.send_message(callback.message.chat.id, 'Начать ли отслеживать объявления?', reply_markup=murkup_wotb)
    elif callback.data == 'y19':
        backwotb_offer = 0
        while True:
            offerwotb_text = parserwotb(backwotb_offer)
            backwotb_offer = offerwotb_text[1]
            if offerwotb_text[0] != None:
                bot.send_message(callback.message.chat.id, offerwotb_text)
                time.sleep(600)
    elif callback.data == 'yt':
        murkup_yt = types.InlineKeyboardMarkup()
        yyt = types.InlineKeyboardButton('Да', callback_data='y20')
        nyt = types.InlineKeyboardButton('Нет', callback_data='no')
        murkup_yt.row(yyt, nyt)
        bot.send_message(callback.message.chat.id, 'Начать ли отслеживать объявления?', reply_markup=murkup_yt)
    elif callback.data == 'y20':
        backyt_offer = 0
        while True:
            offeryt_text = parseryt(backyt_offer)
            backyt_offer = offeryt_text[1]
            if offeryt_text[0] != None:
                bot.send_message(callback.message.chat.id, offeryt_text)
                time.sleep(600)
    elif callback.data == 'tg':
        murkup_tg = types.InlineKeyboardMarkup()
        ytg = types.InlineKeyboardButton('Да', callback_data='y21')
        ntg = types.InlineKeyboardButton('Нет', callback_data='no')
        murkup_tg.row(ytg, ntg)
        bot.send_message(callback.message.chat.id, 'Начать ли отслеживать объявления?', reply_markup=murkup_tg)
    elif callback.data == 'y21':
        backtg_offer = 0
        while True:
            offertg_text = parsertg(backtg_offer)
            backtg_offer = offertg_text[1]
            if offertg_text[0] != None:
                bot.send_message(callback.message.chat.id, offertg_text)
                time.sleep(600)
    elif callback.data == 'vk':
        murkup_vk = types.InlineKeyboardMarkup()
        yvk = types.InlineKeyboardButton('Да', callback_data='y22')
        nvk = types.InlineKeyboardButton('Нет', callback_data='no')
        murkup_vk.row(yvk, nvk)
        bot.send_message(callback.message.chat.id, 'Начать ли отслеживать объявления по продаже сообществ?', reply_markup=murkup_vk)
    elif callback.data == 'y22':
        backvk_offer = 0
        while True:
            offervk_text = parservk(backvk_offer)
            backvk_offer = offervk_text[1]
            if offervk_text[0] != None:
                bot.send_message(callback.message.chat.id, offervk_text)
                time.sleep(600)
    elif callback.data == 'ns':
        murkup_ns = types.InlineKeyboardMarkup()
        yns = types.InlineKeyboardButton('Да', callback_data='y23')
        nns = types.InlineKeyboardButton('Нет', callback_data='no')
        murkup_ns.row(yns, nns)
        bot.send_message(callback.message.chat.id, 'Начать ли отслеживать объявления по продаже сообществ?', reply_markup=murkup_ns)
    elif callback.data == 'y23':
        backns_offer = 0
        while True:
            offerns_text = parserns(backns_offer)
            backns_offer = offerns_text[1]
            if offerns_text[0] != None:
                bot.send_message(callback.message.chat.id, offerns_text)
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
def parserark(backark_postid):
    r_arkacc = requests.get("https://funpay.com/lots/327/")
    html_arkacc = BS(r_arkacc.content, 'html.parser')
    offer = html_arkacc.find("a", class_="tc-item")
    ark_postid = offer["data-server"]
    if ark_postid != backark_postid:
        title = offer.find("div", class_="tc-desc-text").text.strip()
        user = offer.find("div", class_="media-user-name").text.strip()
        price = offer.find("div", class_="tc-price").text.strip()
        url = html_arkacc.find("a", class_= "tc-item", href=True)["href"].strip()
        print(title, user, price, url, ark_postid, backark_postid, sep="\n\n")
        return f'{title}\n{user}\n{price}\n{url}'
    else:
        return None, ark_postid
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
def parserrr(backrr_offer):
    r_rracc = requests.get("https://funpay.com/lots/1438/")
    html_rracc = BS(r_rracc.content, 'html.parser')
    offer = html_rracc.find("a", class_="tc-item")
    if offer != backrr_offer:
        title = offer.find("div", class_="tc-desc-text").text.strip()
        user = offer.find("div", class_="media-user-name").text.strip()
        price = offer.find("div", class_="tc-price").text.strip()
        url = html_rracc.find("a", class_= "tc-item", href=True)["href"].strip()
        print(title, user, price, url, sep="\n\n")
        return f'{title}\n{user}\n{price}\n{url}'
    else:
        return None, offer
def parserru(backru_offer):
    r_ruacc = requests.get("https://funpay.com/lots/250/")
    html_ruacc = BS(r_ruacc.content, 'html.parser')
    offer = html_ruacc.find("a", class_="tc-item")
    if offer != backru_offer:
        title = offer.find("div", class_="tc-desc-text").text.strip()
        user = offer.find("div", class_="media-user-name").text.strip()
        price = offer.find("div", class_="tc-price").text.strip()
        url = html_ruacc.find("a", class_= "tc-item", href=True)["href"].strip()
        print(title, user, price, url, sep="\n\n")
        return f'{title}\n{user}\n{price}\n{url}'
    else:
        return None, offer
def parserwt(backwt_offer):
    r_wtacc = requests.get("https://funpay.com/lots/242/")
    html_wtacc = BS(r_wtacc.content, 'html.parser')
    offer = html_wtacc.find("a", class_="tc-item")
    if offer != backwt_offer:
        title = offer.find("div", class_="tc-desc-text").text.strip()
        user = offer.find("div", class_="media-user-name").text.strip()
        price = offer.find("div", class_="tc-price").text.strip()
        url = html_wtacc.find("a", class_= "tc-item", href=True)["href"].strip()
        print(title, user, price, url, sep="\n\n")
        return f'{title}\n{user}\n{price}\n{url}'
    else:
        return None, offer
def parserwf(backwf_offer):
    r_wfacc = requests.get("https://funpay.com/lots/146/")
    html_wfacc = BS(r_wfacc.content, 'html.parser')
    offer = html_wfacc.find("a", class_="tc-item")
    if offer != backwf_offer:
        title = offer.find("div", class_="tc-desc-text").text.strip()
        user = offer.find("div", class_="media-user-name").text.strip()
        price = offer.find("div", class_="tc-price").text.strip()
        url = html_wfacc.find("a", class_= "tc-item", href=True)["href"].strip()
        print(title, user, price, url, sep="\n\n")
        return f'{title}\n{user}\n{price}\n{url}'
    else:
        return None, offer
def parserwot(backwot_offer):
    r_wotacc = requests.get("https://funpay.com/lots/77/")
    html_wotacc = BS(r_wotacc.content, 'html.parser')
    offer = html_wotacc.find("a", class_="tc-item")
    if offer != backwot_offer:
        title = offer.find("div", class_="tc-desc-text").text.strip()
        user = offer.find("div", class_="media-user-name").text.strip()
        price = offer.find("div", class_="tc-price").text.strip()
        url = html_wotacc.find("a", class_= "tc-item", href=True)["href"].strip()
        print(title, user, price, url, sep="\n\n")
        return f'{title}\n{user}\n{price}\n{url}'
    else:
        return None, offer
def parserwotb(backwotb_offer):
    r_wotbacc = requests.get("https://funpay.com/lots/288/")
    html_wotbacc = BS(r_wotbacc.content, 'html.parser')
    offer = html_wotbacc.find("a", class_="tc-item")
    if offer != backwotb_offer:
        title = offer.find("div", class_="tc-desc-text").text.strip()
        user = offer.find("div", class_="media-user-name").text.strip()
        price = offer.find("div", class_="tc-price").text.strip()
        url = html_wotbacc.find("a", class_= "tc-item", href=True)["href"].strip()
        print(title, user, price, url, sep="\n\n")
        return f'{title}\n{user}\n{price}\n{url}'
    else:
        return None, offer
def parseryt(backyt_offer):
    r_ytacc = requests.get("https://funpay.com/lots/700/")
    html_ytacc = BS(r_ytacc.content, 'html.parser')
    offer = html_ytacc.find("a", class_="tc-item")
    if offer != backyt_offer:
        title = offer.find("div", class_="tc-desc-text").text.strip()
        user = offer.find("div", class_="media-user-name").text.strip()
        price = offer.find("div", class_="tc-price").text.strip()
        url = html_ytacc.find("a", class_= "tc-item", href=True)["href"].strip()
        print(title, user, price, url, sep="\n\n")
        return f'{title}\n{user}\n{price}\n{url}'
    else:
        return None, offer
def parsertg(backtg_offer):
    r_tgacc = requests.get("https://funpay.com/lots/2424/")
    html_tgacc = BS(r_tgacc.content, 'html.parser')
    offer = html_tgacc.find("a", class_="tc-item")
    if offer != backtg_offer:
        title = offer.find("div", class_="tc-desc-text").text.strip()
        user = offer.find("div", class_="media-user-name").text.strip()
        price = offer.find("div", class_="tc-price").text.strip()
        url = html_tgacc.find("a", class_= "tc-item", href=True)["href"].strip()
        print(title, user, price, url, sep="\n\n")
        return f'{title}\n{user}\n{price}\n{url}'
    else:
        return None, offer
def parservk(backvk_offer):
    r_vkacc = requests.get("https://funpay.com/lots/699/")
    html_vkacc = BS(r_vkacc.content, 'html.parser')
    offer = html_vkacc.find("a", class_="tc-item")
    if offer != backvk_offer:
        title = offer.find("div", class_="tc-desc-text").text.strip()
        user = offer.find("div", class_="media-user-name").text.strip()
        price = offer.find("div", class_="tc-price").text.strip()
        url = html_vkacc.find("a", class_= "tc-item", href=True)["href"].strip()
        print(title, user, price, url, sep="\n\n")
        return f'{title}\n{user}\n{price}\n{url}'
    else:
        return None, offer
def parserns(backns_offer):
    r_nsacc = requests.get("https://funpay.com/lots/1318/")
    html_nsacc = BS(r_nsacc.content, 'html.parser')
    offer = html_nsacc.find("a", class_="tc-item")
    if offer != backns_offer:
        title = offer.find("div", class_="tc-desc-text").text.strip()
        user = offer.find("div", class_="media-user-name").text.strip()
        price = offer.find("div", class_="tc-price").text.strip()
        url = html_nsacc.find("a", class_= "tc-item", href=True)["href"].strip()
        print(title, user, price, url, sep="\n\n")
        return f'{title}\n{user}\n{price}\n{url}'
    else:
        return None, offer

bot.polling(none_stop=True)