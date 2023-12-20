import telebot 
from telebot import types
bot = telebot.TeleBot('6605974541:AAHK8C1ZwDC4JpTNqfC-Fvxhm4ucCqJnbLo')

gamelist = ['ARK: Survival Evolved', 'Black Russia', 'Brawl Stars', 'CarX Drift Racing', 'Counter-Strike 2', 'Crossout', 'Cyberpunk 2077', 'Dead by Daylight', 'Dota 2', 'Dying Light 2', 'GTA5', 'Hearts of Iron IV', 'Minecraft', 'Mobile Legends', 'PUBG', 'PUBG Mobile', 'Radmir', 'Rust', 'War Thunder', 'Warface', 'World of Tanks', 'World of Tanks Blitz','YouTube', 'Telegram Premium', 'ВК', 'Netflix']

@bot.message_handler(commands=['start'])
def cmd_start(message):
    markup_re = types.ReplyKeyboardMarkup()
    button1 = types.KeyboardButton('Выбрать игру')
    button2 = types.KeyboardButton('Избранные категории')
    markup_re.row(button1, button2)
    bot.send_message(message.chat.id, 'Добро пожаловать в телеграмм бот - парсер игровой биржи <b>FunPay! Для большей информации - /help</b>', parse_mode='html', reply_markup=markup_re)
    bot.register_next_step_handler(message, on_click)

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
    elif message.text == 'Избранные категории':
        bot.send_message(message.chat.id, 'Не заходи сюда!')

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'ark':
        murkup_ark = types.InlineKeyboardMarkup()
        category1_ark = types.InlineKeyboardButton('Аккаунты📑', callback_data='acc1')
        category2_ark = types.InlineKeyboardButton('Ключи🗝', callback_data='keys1')
        category3_ark = types.InlineKeyboardButton('Предметы🎲', callback_data='predm1')
        category4_ark = types.InlineKeyboardButton('Услуги✔', callback_data='uslug1')
        murkup_ark.row(category1_ark, category2_ark)
        murkup_ark.row(category3_ark, category4_ark)
        bot.send_message(callback.message.chat.id, 'Хороший выбор!👍 Теперь выберите категорию📝', reply_markup=murkup_ark)
    elif callback.data == 'br':
        murkup_br = types.InlineKeyboardMarkup()
        category1_br = types.InlineKeyboardButton('Вирты💵', callback_data='virts2')
        category2_br = types.InlineKeyboardButton('Аккаунты📑', callback_data='acc2')
        category3_br = types.InlineKeyboardButton('Донат💲', callback_data='donat2')
        category4_br = types.InlineKeyboardButton('Предметы🎲', callback_data='predm2')
        category5_br = types.InlineKeyboardButton('Услуги✔', callback_data='uslug2')
        category6_br = types.InlineKeyboardButton('Прочее▶', callback_data='more2')
        murkup_br.row(category1_br, category2_br)
        murkup_br.row(category3_br, category4_br)
        murkup_br.row(category5_br, category6_br)
        bot.send_message(callback.message.chat.id, 'Хороший выбор!👍 Теперь выберите категорию📝', reply_markup=murkup_br)
    elif callback.data == 'carx':
        murkup_carx = types.InlineKeyboardMarkup()
        category1_carx = types.InlineKeyboardButton('Аккаунты📑', callback_data='acc3')
        category2_carx = types.InlineKeyboardButton('Ключи🗝', callback_data='keys3')
        category3_carx = types.InlineKeyboardButton('Донат💲', callback_data='donat3')
        category4_carx = types.InlineKeyboardButton('Услуги✔', callback_data='uslug3')
        murkup_carx.row(category1_carx, category2_carx)
        murkup_carx.row(category3_carx, category4_carx)
        bot.send_message(callback.message.chat.id, 'Хороший выбор!👍 Теперь выберите категорию📝', reply_markup=murkup_carx)
    elif callback.data == 'cs':
        murkup_cs = types.InlineKeyboardMarkup()
        category1_cs = types.InlineKeyboardButton('Аккаунты📑', callback_data='acc4')
        category2_cs = types.InlineKeyboardButton('Prime💎', callback_data='prime')
        category3_cs = types.InlineKeyboardButton('Скины👕👖', callback_data='skin4')
        category4_cs = types.InlineKeyboardButton('Буст📈', callback_data='boost4')
        category5_cs = types.InlineKeyboardButton('Обучение🤓', callback_data='help4')
        category6_cs = types.InlineKeyboardButton('Прочее▶', callback_data='more4')
        murkup_cs.row(category1_cs, category2_cs)
        murkup_cs.row(category3_cs, category4_cs)
        murkup_cs.row(category5_cs, category6_cs)
        bot.send_message(callback.message.chat.id, 'Хороший выбор!👍 Теперь выберите категорию📝', reply_markup=murkup_cs)
    elif callback.data == 'cr':
        murkup_cr = types.InlineKeyboardMarkup()
        category1_cr = types.InlineKeyboardButton('Аккаунты📑', callback_data='acc5')
        category2_cr = types.InlineKeyboardButton('Монеты💵', callback_data='money5')
        category3_cr = types.InlineKeyboardButton('Предметы🎲', callback_data='predm5')
        category4_cr = types.InlineKeyboardButton('Услуги✔', callback_data='uslug5')
        murkup_cr.row(category1_cr, category2_cr)
        murkup_cr.row(category3_cr, category4_cr)
        bot.send_message(callback.message.chat.id, 'Хороший выбор!👍 Теперь выберите категорию📝', reply_markup=murkup_cr)
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
    elif callback.data == 'dbd':
        murkup_dbd = types.InlineKeyboardMarkup()
        category1_dbd = types.InlineKeyboardButton('Аккаунты📑', callback_data='acc6')
        category2_dbd = types.InlineKeyboardButton('Ключи🗝', callback_data='keys6')
        category3_dbd = types.InlineKeyboardButton('Золотые клетки⛓', callback_data='gold6')
        category4_dbd = types.InlineKeyboardButton('Буст📈', callback_data='boost6')
        category5_dbd = types.InlineKeyboardButton('Обучение🤓', callback_data='help6')
        category6_dbd = types.InlineKeyboardButton('Prime Gaming💎', callback_data='prime6')
        category7_dbd = types.InlineKeyboardButton('Game pass', callback_data='pass6')
        category8_dbd = types.InlineKeyboardButton('Прочее▶', callback_data='more6')
        murkup_dbd.row(category1_dbd, category2_dbd)
        murkup_dbd.row(category3_dbd, category4_dbd)
        murkup_dbd.row(category5_dbd, category6_dbd)
        murkup_dbd.row(category7_dbd, category8_dbd)
        bot.send_message(callback.message.chat.id, 'Хороший выбор!👍 Теперь выберите категорию📝', reply_markup=murkup_dbd)
    elif callback.data == 'dota':
        murkup_dota = types.InlineKeyboardMarkup()
        category1_dota = types.InlineKeyboardButton('Аккаунты📑', callback_data='acc7')
        category2_dota = types.InlineKeyboardButton('Привязки VHS', callback_data='priv7')
        category3_dota = types.InlineKeyboardButton('Предметы🎲', callback_data='predm7')
        category4_dota = types.InlineKeyboardButton('Буст MMR📈', callback_data='boost7')
        category5_dota = types.InlineKeyboardButton('Калибровка', callback_data='kal7')
        category6_dota = types.InlineKeyboardButton('Отмыв ЛП', callback_data='lp7')
        category7_dota = types.InlineKeyboardButton('Обучение🤓', callback_data='help7')
        np_dota = types.InlineKeyboardButton('Следующая страница>>', callback_data='npc1')
        murkup_dota.row(category1_dota, category2_dota)
        murkup_dota.row(category3_dota, category4_dota)
        murkup_dota.row(category5_dota, category6_dota)
        murkup_dota.row(category7_dota, np_dota)
        bot.send_message(callback.message.chat.id, 'Хороший выбор!👍 Теперь выберите категорию📝', reply_markup=murkup_dota)
    elif callback.data == 'dl':
        murkup_dl = types.InlineKeyboardMarkup()
        category1_dl = types.InlineKeyboardButton('Аккаунты📑', callback_data='acc8')
        category2_dl = types.InlineKeyboardButton('Ключи🗝', callback_data='keys8')
        category3_dl = types.InlineKeyboardButton('Twitch Drops', callback_data='twitch8')
        category4_dl = types.InlineKeyboardButton('Услуги✔', callback_data='uslug8')
        murkup_dl.row(category1_dl, category2_dl)
        murkup_dl.row(category4_dl, category3_dl)
        bot.send_message(callback.message.chat.id, 'Хороший выбор!👍 Теперь выберите категорию📝', reply_markup=murkup_dl)
    elif callback.data == 'gta':
        murkup_gta = types.InlineKeyboardMarkup()
        category1_gta = types.InlineKeyboardButton('Аккаунты📑', callback_data='acc9')
        category2_gta = types.InlineKeyboardButton('Деньги💵', callback_data='money9')
        category3_gta = types.InlineKeyboardButton('Ключи🗝', callback_data='keys9')
        category4_gta = types.InlineKeyboardButton('Услуги✔', callback_data='uslug9')
        category5_gta = types.InlineKeyboardButton('Прочее▶', callback_data='more9')
        murkup_gta.row(category2_gta, category1_gta)
        murkup_gta.row(category3_gta, category4_gta)
        murkup_gta.row(category5_gta)
        bot.send_message(callback.message.chat.id, 'Хороший выбор!👍 Теперь выберите категорию📝', reply_markup=murkup_gta)
    elif callback.data == 'hoi':
        murkup_hoi = types.InlineKeyboardMarkup()
        category1_hoi = types.InlineKeyboardButton('Аккаунты📑', callback_data='acc10')
        category2_hoi = types.InlineKeyboardButton('Ключи🗝', callback_data='keys10')
        category3_hoi = types.InlineKeyboardButton('Услуги✔', callback_data='uslug10')
        category4_hoi = types.InlineKeyboardButton('Оффлайн активации', callback_data='offline')
        murkup_hoi.row(category1_hoi, category2_hoi)
        murkup_hoi.row(category3_hoi, category4_hoi)
        bot.send_message(callback.message.chat.id, 'Хороший выбор!👍 Теперь выберите категорию📝', reply_markup=murkup_hoi)
    elif callback.data == 'mn':
        murkup_mn = types.InlineKeyboardMarkup()
        category1_mn = types.InlineKeyboardButton('Аккаунты📑', callback_data='acc11')
        category2_mn = types.InlineKeyboardButton('Ключи🗝', callback_data='keys11')
        category3_mn = types.InlineKeyboardButton('Minecoins', callback_data='mine')
        category4_mn = types.InlineKeyboardButton('Валюта💵', callback_data='money11')
        category5_mn = types.InlineKeyboardButton('Донат💲', callback_data='donat11')
        category6_mn = types.InlineKeyboardButton('Предметы🎲', callback_data='predm11')
        category7_mn = types.InlineKeyboardButton('Услуги✔', callback_data='uslug11')
        np_mn = types.InlineKeyboardButton('Следующая страница>>', callback_data='npc2')
        murkup_mn.row(category1_mn, category2_mn)
        murkup_mn.row(category3_mn, category4_mn)
        murkup_mn.row(category5_mn, category6_mn)
        murkup_mn.row(category7_mn, np_mn)
        bot.send_message(callback.message.chat.id, 'Хороший выбор!👍 Теперь выберите категорию📝', reply_markup=murkup_mn)
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
    elif callback.data == 'mb':
        murkup_mb = types.InlineKeyboardMarkup()
        category1_mb = types.InlineKeyboardButton('Аккаунты📑', callback_data='acc12')
        category2_mb = types.InlineKeyboardButton('Алмазы💰', callback_data='money12')
        category3_mb = types.InlineKeyboardButton('Донат💲', callback_data='donat12')
        category4_mb = types.InlineKeyboardButton('Буст📈', callback_data='boost12')
        category5_mb = types.InlineKeyboardButton('Подарки', callback_data='pod12')
        category6_mb = types.InlineKeyboardButton('Прочее▶', callback_data='more12')
        murkup_mb.row(category1_mb, category2_mb)
        murkup_mb.row(category3_mb, category4_mb)
        murkup_mb.row(category5_mb, category6_mb)
        bot.send_message(callback.message.chat.id, 'Хороший выбор!👍 Теперь выберите категорию📝', reply_markup=murkup_mb)
    elif callback.data == 'pubg':
        murkup_pubg = types.InlineKeyboardMarkup()
        category1_pubg = types.InlineKeyboardButton('Аккаунты📑', callback_data='acc13')
        category2_pubg = types.InlineKeyboardButton('G-Coins💰', callback_data='money13')
        category3_pubg = types.InlineKeyboardButton('Предметы🎲', callback_data='predm13')
        category4_pubg = types.InlineKeyboardButton('Услуги✔', callback_data='uslug13')
        category5_pubg = types.InlineKeyboardButton('Prime Gaming💎', callback_data='prime13')
        category6_pubg = types.InlineKeyboardButton('Twitch Drops', callback_data='twitch13')
        category7_pubg = types.InlineKeyboardButton('Прочее', callback_data='more13')
        murkup_pubg.row(category1_pubg, category2_pubg)
        murkup_pubg.row(category3_pubg, category4_pubg)
        murkup_pubg.row(category5_pubg, category6_pubg)
        murkup_pubg.row(category7_pubg)
        bot.send_message(callback.message.chat.id, 'Хороший выбор!👍 Теперь выберите категорию📝', reply_markup=murkup_pubg)
    elif callback.data == 'pubgm':
        murkup_pubgm = types.InlineKeyboardMarkup()
        category1_pubgm = types.InlineKeyboardButton('Аккаунты📑', callback_data='acc14')
        category2_pubgm = types.InlineKeyboardButton('UC💵', callback_data='money14')
        category3_pubgm = types.InlineKeyboardButton('Донат💲', callback_data='donat14')
        category4_pubgm = types.InlineKeyboardButton('Буст📈', callback_data='boost14')
        category5_pubgm = types.InlineKeyboardButton('Достижения', callback_data='dost14')
        category6_pubgm = types.InlineKeyboardButton('Metro Royale', callback_data='metroyal14')
        category7_pubgm = types.InlineKeyboardButton('Prime Gaming💎', callback_data='prime14')
        np_pubgm = types.InlineKeyboardButton('Следующая страница>>', callback_data='npc3')
        murkup_pubgm.row(category1_pubgm, category2_pubgm)
        murkup_pubgm.row(category3_pubgm, category4_pubgm)
        murkup_pubgm.row(category5_pubgm, category6_pubgm)
        murkup_pubgm.row(category7_pubgm, np_pubgm)
        bot.send_message(callback.message.chat.id, 'Хороший выбор!👍 Теперь выберите категорию📝', reply_markup=murkup_pubgm)
    elif callback.data == 'rr':
        murkup_rr = types.InlineKeyboardMarkup()
        category1_rr = types.InlineKeyboardButton('Вирты💵', callback_data='virts15')
        category2_rr = types.InlineKeyboardButton('Аккаунты📑', callback_data='acc15')
        category3_rr = types.InlineKeyboardButton('Донат💲', callback_data='donat15')
        category4_rr = types.InlineKeyboardButton('Предметы🎲', callback_data='predm15')
        category5_rr = types.InlineKeyboardButton('Услуги✔', callback_data='uslug15')
        category6_rr = types.InlineKeyboardButton('Прочее▶', callback_data='more15')
        murkup_rr.row(category1_rr, category2_rr)
        murkup_rr.row(category3_rr, category4_rr)
        murkup_rr.row(category5_rr, category6_rr)
        bot.send_message(callback.message.chat.id, 'Хороший выбор!👍 Теперь выберите категорию📝', reply_markup=murkup_rr)
    elif callback.data == 'ru':
        murkup_ru = types.InlineKeyboardMarkup()
        category1_ru = types.InlineKeyboardButton('Аккаунты📑', callback_data='acc16')
        category2_ru = types.InlineKeyboardButton('Ключи🗝', callback_data='keys16')
        category3_ru = types.InlineKeyboardButton('Монеты', callback_data='money16')
        category4_ru = types.InlineKeyboardButton('Предметы🎲', callback_data='predm16')
        category5_ru = types.InlineKeyboardButton('Услуги✔', callback_data='uslug16')
        category6_ru = types.InlineKeyboardButton('VIP пропуск💎', callback_data='vip16')
        category7_ru = types.InlineKeyboardButton('Twitch Drops', callback_data='twitch16')
        category8_ru = types.InlineKeyboardButton('Прочее▶', callback_data='more16')
        murkup_ru.row(category1_ru, category2_ru)
        murkup_ru.row(category3_ru, category4_ru)
        murkup_ru.row(category5_ru, category6_ru)
        murkup_ru.row(category7_ru, category8_ru)
        bot.send_message(callback.message.chat.id, 'Хороший выбор!👍 Теперь выберите категорию📝', reply_markup=murkup_ru)
    elif callback.data == 'wt':
        murkup_wt = types.InlineKeyboardMarkup()
        category1_wt = types.InlineKeyboardButton('Фарм серебра💵', callback_data='money17')
        category2_wt = types.InlineKeyboardButton('Аккаунты📑', callback_data='acc17')
        category3_wt = types.InlineKeyboardButton('Прокачка📈', callback_data='boost17')
        category4_wt = types.InlineKeyboardButton('Бонус-коды', callback_data='bonus17')
        category5_wt = types.InlineKeyboardButton('Прочее▶', callback_data='more17')
        murkup_wt.row(category2_wt, category1_wt)
        murkup_wt.row(category3_wt, category4_wt)
        murkup_wt.row(category5_wt)
        bot.send_message(callback.message.chat.id, 'Хороший выбор!👍 Теперь выберите категорию📝', reply_markup=murkup_wt)
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
    elif callback.data == 'wf':
        murkup_wf = types.InlineKeyboardMarkup()
        category1_wf = types.InlineKeyboardButton('Аккаунты📑', callback_data='acc18')
        category3_wf = types.InlineKeyboardButton('Буст PM📈', callback_data='boost118')
        category2_wf = types.InlineKeyboardButton('Предметы🎲', callback_data='predm18')
        category4_wf = types.InlineKeyboardButton('Буст спецопераций📈', callback_data='boost218')
        category5_wf = types.InlineKeyboardButton('Буст побед📈', callback_data='boost318')
        category6_wf = types.InlineKeyboardButton('Буст статистики📈', callback_data='boost418')
        category7_wf = types.InlineKeyboardButton('Кредиты💵', callback_data='money18')
        np_wf = types.InlineKeyboardButton('Следующая страница>>', callback_data='npc4')
        murkup_wf.row(category1_wf, category2_wf)
        murkup_wf.row(category3_wf, category4_wf)
        murkup_wf.row(category5_wf, category6_wf)
        murkup_wf.row(category7_wf, np_wf)
        bot.send_message(callback.message.chat.id, 'Хороший выбор!👍 Теперь выберите категорию📝', reply_markup=murkup_wf)
    elif callback.data == 'wot':
        murkup_wot = types.InlineKeyboardMarkup()
        category1_wot = types.InlineKeyboardButton('Аккаунты📑', callback_data='acc19')
        category2_wot = types.InlineKeyboardButton('Бонус-коды', callback_data='bonus19')
        category3_wot = types.InlineKeyboardButton('Буст📈', callback_data='boost19')
        category4_wot = types.InlineKeyboardButton('Фарм серебра💵', callback_data='money19')
        category5_wot = types.InlineKeyboardButton('Выполнение ЛБЗ', callback_data='lbz19')
        category6_wot = types.InlineKeyboardButton('Обучение🤓', callback_data='help19')
        category7_wot = types.InlineKeyboardButton('Донат💲', callback_data='donat19')
        np_wot = types.InlineKeyboardButton('Следующая страница>>', callback_data='npc5')
        murkup_wot.row(category1_wot, category2_wot)
        murkup_wot.row(category3_wot, category4_wot)
        murkup_wot.row(category5_wot, category6_wot)
        murkup_wot.row(category7_wot, np_wot)
        bot.send_message(callback.message.chat.id, 'Хороший выбор!👍 Теперь выберите категорию📝', reply_markup=murkup_wot)
    elif callback.data == 'wotb':
        murkup_wotb = types.InlineKeyboardMarkup()
        category1_wotb = types.InlineKeyboardButton('Аккаунты📑', callback_data='acc20')
        category2_wotb = types.InlineKeyboardButton('Буст📈', callback_data='boost20')
        category3_wotb = types.InlineKeyboardButton('Фарм серебра💵', callback_data='money20')
        category4_wotb = types.InlineKeyboardButton('Обучение🤓', callback_data='help20')
        category5_wotb = types.InlineKeyboardButton('Золото💰', callback_data='gold20')
        category6_wotb = types.InlineKeyboardButton('Донат💲', callback_data='donat20')
        category7_wotb = types.InlineKeyboardButton('Бонус-коды', callback_data='bonus20')
        category9_wotb = types.InlineKeyboardButton('Прочее▶', callback_data='more20')
        category8_wotb = types.InlineKeyboardButton('Кланы👨‍💻', callback_data='clan20')
        murkup_wotb.row(category1_wotb, category2_wotb)
        murkup_wotb.row(category3_wotb, category4_wotb)
        murkup_wotb.row(category5_wotb, category6_wotb)
        murkup_wotb.row(category7_wotb, category8_wotb)
        murkup_wotb.row(category9_wotb)
        bot.send_message(callback.message.chat.id, 'Хороший выбор!👍 Теперь выберите категорию📝', reply_markup=murkup_wotb)
    elif callback.data == 'yt':
        murkup_yt = types.InlineKeyboardMarkup()
        category1_yt = types.InlineKeyboardButton('Услуги✔', callback_data='uslug21')
        category2_yt = types.InlineKeyboardButton('Канал', callback_data='chan21')
        category3_yt = types.InlineKeyboardButton('Premium💎', callback_data='prime21')
        murkup_yt.row(category1_yt, category2_yt)
        murkup_yt.row(category3_yt)
        bot.send_message(callback.message.chat.id, 'Хороший выбор!👍 Теперь выберите категорию📝', reply_markup=murkup_yt)
    elif callback.data == 'tg':
        murkup_tg = types.InlineKeyboardMarkup()
        category1_tg = types.InlineKeyboardButton('Каналы', callback_data='chan22')
        category2_tg = types.InlineKeyboardButton('Услуги✔', callback_data='uslug22')
        category3_tg = types.InlineKeyboardButton('Premium💎', callback_data='prime22')
        category4_tg = types.InlineKeyboardButton('Прочее▶', callback_data='more22')
        murkup_tg.row(category1_tg, category2_tg)
        murkup_tg.row(category3_tg, category4_tg)
        bot.send_message(callback.message.chat.id, 'Хороший выбор!👍 Теперь выберите категорию📝', reply_markup=murkup_tg)
    elif callback.data == 'vk':
        murkup_vk = types.InlineKeyboardMarkup()
        category1_vk = types.InlineKeyboardButton('Услуги✔', callback_data='uslug23')
        category2_vk = types.InlineKeyboardButton('Сообщества', callback_data='chan23')
        murkup_vk.row(category1_vk, category2_vk)
        bot.send_message(callback.message.chat.id, 'Хороший выбор!👍 Теперь выберите категорию📝', reply_markup=murkup_vk)
    elif callback.data == 'p5':
        murkup_5page = types.InlineKeyboardMarkup()
        game25 = types.InlineKeyboardButton('Netflix', callback_data='ns')
        prevp4 = types.InlineKeyboardButton('<<Предыдущая страница', callback_data='p4')
        murkup_5page.row(game25)
        murkup_5page.row(prevp4)
        bot.send_message(callback.message.chat.id, '🏀Выберите игру из списка ниже! 5 страница', reply_markup=murkup_5page)
    elif callback.data == 'ns':
        murkup_ns = types.InlineKeyboardMarkup()
        category1_ns = types.InlineKeyboardButton('Аккаунты📑', callback_data='acc24')
        category2_ns = types.InlineKeyboardButton('Подписка', callback_data='sub24')
        category3_ns = types.InlineKeyboardButton('Подарочные карты', callback_data='card24')
        murkup_ns.row(category1_ns, category2_ns)
        murkup_ns.row(category3_ns)
        bot.send_message(callback.message.chat.id, 'Хороший выбор!👍 Теперь выберите категорию📝', reply_markup=murkup_ns)
    elif callback.data == 'p1':
        murkup2_page1 = types.InlineKeyboardMarkup()
        game1 = types.InlineKeyboardButton('ARK', callback_data='ark')
        game2 = types.InlineKeyboardButton('Black Russia', callback_data='br')
        game3 = types.InlineKeyboardButton('Brawl Stars', callback_data='bs')
        game4 = types.InlineKeyboardButton('CarX', callback_data='carx')
        game5 = types.InlineKeyboardButton('CS Go 2', callback_data='cs')
        game6 = types.InlineKeyboardButton('Crossout', callback_data='cr')
        nextp = types.InlineKeyboardButton('Следующая страница>>', callback_data='p2')
        murkup2_page1.row(game1, game2)
        murkup2_page1.row(game3, game4)
        murkup2_page1.row(game5, game6)
        murkup2_page1.row(nextp)
        bot.send_message(callback.message.chat.id, '🎮Выберите игру из списка ниже!', reply_markup=murkup2_page1)
    elif callback.data == 'npc1':
        murkup_dota2 = types.InlineKeyboardMarkup()
        category8_dota = types.InlineKeyboardButton('Услуги Dota+💎', callback_data='uslugdota')
        category9_dota = types.InlineKeyboardButton('Компендиум', callback_data='kompend')
        category10_dota = types.InlineKeyboardButton('Прочее▶', callback_data='more7')
        pp_dota = types.InlineKeyboardButton('<<Предыдущая страница', callback_data='dota')
        murkup_dota2.row(category8_dota, category9_dota)
        murkup_dota2.row(category10_dota, pp_dota)
        bot.send_message(callback.message.chat.id, '2 страница категорий', reply_markup=murkup_dota2)
    elif callback.data == 'npc2':
        murkup_mn2 = types.InlineKeyboardMarkup()
        category8_mn2 = types.InlineKeyboardButton('Game pass', callback_data='pass11')
        category9_mn2 = types.InlineKeyboardButton('Конфиги', callback_data='conf11')
        category10_mn2 = types.InlineKeyboardButton('Гайды', callback_data='guide11')
        category11_mn2 = types.InlineKeyboardButton('Оффлайн активации', callback_data='offline11')
        category12_mn2 = types.InlineKeyboardButton('Прочее▶', callback_data='more11')
        pp_mn2 = types.InlineKeyboardButton('<<Предыдущая страница', callback_data='mn')
        murkup_mn2.row(category8_mn2, category9_mn2)
        murkup_mn2.row(category10_mn2, category11_mn2)
        murkup_mn2.row(category12_mn2, pp_mn2)
        bot.send_message(callback.message.chat.id, '2 страница категорий', reply_markup=murkup_mn2)
    elif callback.data == 'npc3':
        murkup_pubgm2 = types.InlineKeyboardMarkup()
        category8_pubgm2 = types.InlineKeyboardButton('Популярность', callback_data='pop14')
        category9_pubgm2 = types.InlineKeyboardButton('Прочее▶', callback_data='more14')
        pp_pubgm2 = types.InlineKeyboardButton('<<Предыдущая страница', callback_data='pubgm')
        murkup_pubgm2.row(category8_pubgm2, category9_pubgm2)
        murkup_pubgm2.row(pp_pubgm2)
        bot.send_message(callback.message.chat.id, '2 страница категорий', reply_markup=murkup_pubgm2)
    elif callback.data == 'npc4':
        murkup_wf2 = types.InlineKeyboardMarkup()
        category8_wf2 = types.InlineKeyboardButton('Достижения', callback_data='dost18')
        category9_wf2 = types.InlineKeyboardButton('Twitch Drops', callback_data='twitch18')
        category10_wf2 = types.InlineKeyboardButton('Прочее▶', callback_data='more18')
        pp_wf2 = types.InlineKeyboardButton('<<Предыдущая страница', callback_data='wf')
        murkup_wf2.row(category8_wf2, category9_wf2)
        murkup_wf2.row(category10_wf2, pp_wf2)
        bot.send_message(callback.message.chat.id, '2 страница категорий', reply_markup=murkup_wf2)
    elif callback.data == 'npc5':
        murkup_wot2 = types.InlineKeyboardMarkup()
        category8_wot2 = types.InlineKeyboardButton('Золото💰', callback_data='gold19')
        category9_wot2 = types.InlineKeyboardButton('Кланы👨‍💻', callback_data='clans19')
        category10_wot2 = types.InlineKeyboardButton('Коробки🎁', callback_data='box19')
        category11_wot2 = types.InlineKeyboardButton('Prime Gaming💎', callback_data='prime19')
        category12_wot2 = types.InlineKeyboardButton('Twitch Drops', callback_data='twitch19')
        category13_wot2 = types.InlineKeyboardButton('Прочее▶', callback_data='more19')
        pp_wot2 = types.InlineKeyboardButton('<<Предыдущая страница', callback_data='wot')
        murkup_wot2.row(category8_wot2, category9_wot2)
        murkup_wot2.row(category10_wot2, category11_wot2)
        murkup_wot2.row(category12_wot2, category13_wot2)
        murkup_wot2.row(pp_wot2)
        bot.send_message(callback.message.chat.id, '2 страница категорий', reply_markup=murkup_wot2)

bot.polling(none_stop=True)