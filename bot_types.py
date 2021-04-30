import telebot

askgender = telebot.types.ReplyKeyboardMarkup(1, 1)
askgender.row('Я парень', "Я девушка")

askgendersearch = telebot.types.ReplyKeyboardMarkup(1, 1)
askgendersearch.row('Девушек', "Парней")

cities = telebot.types.ReplyKeyboardMarkup(1, 1)
cities.row('Ташкент')

create_username = telebot.types.ReplyKeyboardMarkup(1, 1)
create_username.row('Сейчас создам', 'Продолжить без него')

sex = telebot.types.ReplyKeyboardMarkup(1, 1)
sex.row('Я парень', 'Я девушка')

sex_search = telebot.types.ReplyKeyboardMarkup(1, 1)
sex_search.row('Девушек', 'Парней')

city = telebot.types.ReplyKeyboardMarkup(1, 1)
city.row('Ташкент', 'Другой')

next = telebot.types.ReplyKeyboardMarkup(1, 1)
next.row('Лайк', 'Написать', 'Дальше')
next.add('Стоп')

smash_or_pass = telebot.types.ReplyKeyboardMarkup(1, 1)
smash_or_pass.row("Нравится", "Не нравится")

yesno = ["Не надо", "Давай"]

askyesno = telebot.types.ReplyKeyboardMarkup(1, 1)
askyesno.row(yesno[0], yesno[1])
