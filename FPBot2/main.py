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
        game3 = types.InlineKeyboardButton('Brawl Stars', callback_data='bs')
        game4 = types.InlineKeyboardButton('CarX', callback_data='carx')
        game5 = types.InlineKeyboardButton('CS Go 2', callback_data='cs')
        game6 = types.InlineKeyboardButton('Crossout', callback_data='cr')
        nextp = types.InlineKeyboardButton('Следующая страница>>', callback_data='p2')
        murkup_page1.row(game1, game2)
        murkup_page1.row(game3, game4)
        murkup_page1.row(game5, game6)
        murkup_page1.row(nextp)
        bot.send_message(message.chat.id, '🎮Выберите игру из списка ниже!', reply_markup=murkup_page1)

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'ark':
        bot.send_message(callback.message.chat.id, 'Хороший выбор!👍 Теперь выберите категорию📝')
    elif callback.data == 'br':
        bot.send_message(callback.message.chat.id, 'Хороший выбор!👍 Теперь выберите категорию📝')
    elif callback.data == 'bs':
        bot.send_message(callback.message.chat.id, 'Хороший выбор!👍 Теперь выберите категорию📝')
    elif callback.data == 'carx':
        bot.send_message(callback.message.chat.id, 'Хороший выбор!👍 Теперь выберите категорию📝')
    elif callback.data == 'cs':
        bot.send_message(callback.message.chat.id, 'Хороший выбор!👍 Теперь выберите категорию📝')
    elif callback.data == 'cr':
        bot.send_message(callback.message.chat.id, 'Хороший выбор!👍 Теперь выберите категорию📝')
    elif callback.data == 'p2':
        murkup_2page = types.InlineKeyboardMarkup()
        game7 = types.InlineKeyboardButton('Dead by Daylight', callback_data='dbd')
        game8 = types.InlineKeyboardButton('Dota 2', callback_data='dota')
        game9 = types.InlineKeyboardButton('Dying Light 2', callback_data='dl')
        game10 = types.InlineKeyboardButton('GTA5', callback_data='gta')
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
        bot.send_message(callback.message.chat.id, 'Хороший выбор!👍 Теперь выберите категорию📝')
    elif callback.data == 'dota':
        bot.send_message(callback.message.chat.id, 'Хороший выбор!👍 Теперь выберите категорию📝')
    elif callback.data == 'dl':
        bot.send_message(callback.message.chat.id, 'Хороший выбор!👍 Теперь выберите категорию📝')
    elif callback.data == 'gta':
        bot.send_message(callback.message.chat.id, 'Хороший выбор!👍 Теперь выберите категорию📝')
    elif callback.data == 'hoi':
        bot.send_message(callback.message.chat.id, 'Хороший выбор!👍 Теперь выберите категорию📝')
    elif callback.data == 'mn':
        bot.send_message(callback.message.chat.id, 'Хороший выбор!👍 Теперь выберите категорию📝')
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
        bot.send_message(callback.message.chat.id, 'Хороший выбор!👍 Теперь выберите категорию📝')
    elif callback.data == 'pubg':
        bot.send_message(callback.message.chat.id, 'Хороший выбор!👍 Теперь выберите категорию📝')
    elif callback.data == 'pubgm':
        bot.send_message(callback.message.chat.id, 'Хороший выбор!👍 Теперь выберите категорию📝')
    elif callback.data == 'rr':
        bot.send_message(callback.message.chat.id, 'Хороший выбор!👍 Теперь выберите категорию📝')
    elif callback.data == 'ru':
        bot.send_message(callback.message.chat.id, 'Хороший выбор!👍 Теперь выберите категорию📝')
    elif callback.data == 'wt':
        bot.send_message(callback.message.chat.id, 'Хороший выбор!👍 Теперь выберите категорию📝')
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
        bot.send_message(callback.message.chat.id, 'Хороший выбор!👍 Теперь выберите категорию📝')
    elif callback.data == 'wot':
        bot.send_message(callback.message.chat.id, 'Хороший выбор!👍 Теперь выберите категорию📝')
    elif callback.data == 'wotb':
        bot.send_message(callback.message.chat.id, 'Хороший выбор!👍 Теперь выберите категорию📝')
    elif callback.data == 'yt':
        bot.send_message(callback.message.chat.id, 'Хороший выбор!👍 Теперь выберите категорию📝')
    elif callback.data == 'tg':
        bot.send_message(callback.message.chat.id, 'Хороший выбор!👍 Теперь выберите категорию📝')
    elif callback.data == 'vk':
        bot.send_message(callback.message.chat.id, 'Хороший выбор!👍 Теперь выберите категорию📝')
    elif callback.data == 'p5':
        murkup_5page = types.InlineKeyboardMarkup()
        game25 = types.InlineKeyboardButton('Netflix', callback_data='ns')
        prevp4 = types.InlineKeyboardButton('<<Предыдущая страница', callback_data='p4')
        murkup_5page.row(game25)
        murkup_5page.row(prevp4)
        bot.send_message(callback.message.chat.id, '🏀Выберите игру из списка ниже! 5 страница', reply_markup=murkup_5page)
    elif callback.data == 'ns':
        bot.send_message(callback.message.chat.id, 'Хороший выбор!👍 Теперь выберите категорию📝')
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

bot.polling(none_stop=True)