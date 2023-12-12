import telebot 
from telebot import types
bot = telebot.TeleBot('6605974541:AAHK8C1ZwDC4JpTNqfC-Fvxhm4ucCqJnbLo')

gamelist=['ARK: Survival Evolved', 'Black Russia', 'Brawl Stars', 'CarX Drift Racing', 'Counter-Strike 2', 'Crossout', 'Cyberpunk 2077', 'Dead by Daylight', 'Dota 2', 'Dying Light 2', 'Hearts of Iron IV', 'Minecraft', 'Mob', 'PUBG', 'PUBG Mobile', 'Radmir', 'Rust', 'War Thunder', 'Warface', 'Woorld of Tanks', 'World of Tanks Blitz','YouTube', 'Telegram Premium', 'ВК', 'Netflix']

@bot.message_handler(commands=['start'])
def cmd_start(message):
    markup_re = types.ReplyKeyboardMarkup()
    button1 = types.KeyboardButton('Выбрать игру')
    button2 = types.KeyboardButton('Избранные категории')
    markup_re.row(button1, button2)
    bot.send_message(message.chat.id, 'Добро пожаловать в телеграмм бот - парсер игровой биржи <b>FunPay! Для большей информации - /help</b>', parse_mode='html', reply_markup=markup_re)
    bot.register_next_step_handler(message, on_click)
def on_click(message):
    if message.text == 'Выбрать игру':
        bot.send_message(message.chat.id, 'Напишите название в чат так, как она указана в списке игр, чтобы посмотреть список игр /help')

@bot.message_handler(commands=['help'])
def cmd_start(message):
    murkup = types.InlineKeyboardMarkup()
    murkup.add(types.InlineKeyboardButton('Перечень популярных игр', callback_data='help'))
    bot.send_message(message.chat.id, 'Данный бот создан для парсинга <u>самых популярных игр</u> с биржи <b>FunPay</b>, здесь вы можете подобрать для себя самый лучший вариант какой либо услуги по цене/качеству', parse_mode='html', reply_markup=murkup)

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'help':
        bot.send_message(callback.message.chat.id, 'В перечень входят такие игры как: ARK: Survival Evolved, Black Russia, Brawl Stars, CarX Drift Racing, Counter-Strike 2, Crossout, Cyberpunk 2077, Dead by Daylight, Dota 2, Dying Light 2, Hearts of Iron IV, Minecraft, Mobile Legends, PUBG, PUBG Mobile, Radmir, Rust, War Thunder, Warface, World of Tanks, World of Tanks Blitz. Так-же доступен парсинг каналов YouTube, Telegram Premium, Подписок на ВК и Кинотеатры')

 



bot.polling(none_stop=True)