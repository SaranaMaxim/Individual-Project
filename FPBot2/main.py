import telebot 
from telebot import types
bot = telebot.TeleBot('6605974541:AAHK8C1ZwDC4JpTNqfC-Fvxhm4ucCqJnbLo')

gamelist = ['ARK: Survival Evolved', 'Black Russia', 'Brawl Stars', 'CarX Drift Racing', 'Counter-Strike 2', 'Crossout', 'Cyberpunk 2077', 'Dead by Daylight', 'Dota 2', 'Dying Light 2', 'GTA5', 'Hearts of Iron IV', 'Minecraft', 'Mobile Legends', 'PUBG', 'PUBG Mobile', 'Radmir', 'Rust', 'War Thunder', 'Warface', 'World of Tanks', 'World of Tanks Blitz','YouTube', 'Telegram Premium', 'ВК', 'Netflix']
game = 0
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
#    murkup = types.InlineKeyboardMarkup()
#    murkup.add(types.InlineKeyboardButton('Перечень популярных игр', callback_data='help'))
    bot.send_message(message.chat.id, 'Данный бот создан для парсинга <u>самых популярных игр</u> с биржи <b>FunPay</b>, здесь вы можете подобрать для себя самый лучший вариант какой либо услуги по цене/качеству', parse_mode='html', reply_markup=murkup)

@bot.message_handler(content_types='text')
def on_click(message):
    if message.text == 'Выбрать игру':
        murkup = types.InlineKeyboardMarkup()
        game1 = types.InlineKeyboardButton('ARK', callback_data='ark')
        game2 = types.InlineKeyboardButton('Black Russia', callback_data='br')
        game3 = types.InlineKeyboardButton('Brawl Stars', callback_data='bs')
        game4 = types.InlineKeyboardButton('CarX', callback_data='carx')
        game5 = types.InlineKeyboardButton('CS Go 2', callback_data='cs')
        game6 = types.InlineKeyboardButton('Crossout', callback_data='cr')
        nextp = types.InlineKeyboardButton('Следующая страница>>', callback_data='np')
        murkup.row(game1, game2)
        murkup.row(game3, game4)
        murkup.row(game5, game6)
        murkup.row(nextp)
        bot.send_message(message.chat.id, 'Выберите игру из списка ниже!', reply_markup=murkup)
#        bot.register_next_step_handler(message, game_choose)
#def game_choose(message):
#    if message.text in gamelist:
#        game = gamelist.index(message.text)
#        bot.send_message(message.chat.id, 'Хороший выбор! Теперь выберите категорию')

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
#    if callback.data == 'help':
#        bot.send_message(callback.message.chat.id, 'В перечень входят такие игры как: ARK: Survival Evolved, Black Russia, Brawl Stars, CarX Drift Racing, Counter-Strike 2, Crossout, Cyberpunk 2077, Dead by Daylight, Dota 2, Dying Light 2, GTA5, Hearts of Iron IV, Minecraft, Mobile Legends, PUBG, PUBG Mobile, Radmir, Rust, War Thunder, Warface, World of Tanks, World of Tanks Blitz. Так-же доступен парсинг каналов YouTube, Telegram Premium, Подписок на ВК и Netflix')
    if callback.data == 'ark':
        bot.send_message(callback.message.chat.id, 'Хороший выбор! Теперь выберите категорию')
    elif callback.data == 'br':
        bot.send_message(callback.message.chat.id, 'Хороший выбор! Теперь выберите категорию')
    elif callback.data == 'bs':
        bot.send_message(callback.message.chat.id, 'Хороший выбор! Теперь выберите категорию')
    elif callback.data == 'carx':
        bot.send_message(callback.message.chat.id, 'Хороший выбор! Теперь выберите категорию')
    elif callback.data == 'cs':
        bot.send_message(callback.message.chat.id, 'Хороший выбор! Теперь выберите категорию')
    elif callback.data == 'cr':
        bot.send_message(callback.message.chat.id, 'Хороший выбор! Теперь выберите категорию')
    elif callback.data == 'np':
        murkup_2page = types.InlineKeyboardMarkup()
        game7 = types.InlineKeyboardButton('Dead by Daylight', callback_data='dbd')
        game8 = types.InlineKeyboardButton('Dota 2', callback_data='dota')
        game9 = types.InlineKeyboardButton('Dying Light 2', callback_data='dl')
        game10 = types.InlineKeyboardButton('GTA5', callback_data='gta')
        game11 = types.InlineKeyboardButton('HoI IV', callback_data='hoi')
        game12 = types.InlineKeyboardButton('Minecraft', callback_data='mn')
        nextp2 = types.InlineKeyboardButton('Следующая страница>>', callback_data='mb')
        murkup_2page.row(game8, game9)
        murkup_2page.row(game10, game11)
        murkup_2page.row(game12, game13)
        murkup_2page.row(nextp2)
        bot.send_message(callback.message.chat.id, 'Выберите игру из списка ниже!  2 страница', reply_markup=murkup_2page)

bot.polling(none_stop=True)