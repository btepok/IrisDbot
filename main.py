import telebot
import time
import bot_phrases
import bot_types
import db_manage
import sys

try:
    with open('token.txt') as token_file:
        token = token_file.read()
        bot = telebot.TeleBot(token)
except Exception as error:
    print('Token file is missing or corrupted: ', error)
    sys.exit()


yes_no = telebot.types.ReplyKeyboardMarkup(1, 1)
yes_no.row('Да', 'Нет')


def is_text(message):
    try:
        message.text.lower()
        return True
    except Exception as e:
        print(e)
        return False


def send_mes(message, text):
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['my_acc'])
def user_acc(message, with_mes=True):
    chat_id = message.chat.id
    acc_info = db_manage.select_by_id(chat_id)

    photo = acc_info['photo']
    if with_mes:
        send_mes(message, 'Так выглядит твоя анкета:')
        bot.send_photo(chat_id, photo, caption=f'{acc_info["name"]}, {acc_info["age"]}, {acc_info["city"]} \n \n'
                                               f'{acc_info["description"]}')



@bot.message_handler(commands=['start'])
def start_message(message, first=True):
    db_manage.likes_db(message.chat.id)
    if db_manage.is_exist(message.chat.id):
        send_mes(message, 'Ты уже есть у нас:')
        user_acc(message)
        if message.chat.username == None:
            print('asd')
    else:
        if first:
            bot.send_message(message.chat.id, bot_phrases.hello_random(), reply_markup=bot_types.askyesno)
            bot.send_sticker(message.chat.id, bot_phrases.hello_sticker())
        else:
            bot.send_message(message.chat.id, 'Перейдём к регистрации?', reply_markup=bot_types.askyesno)

        if message.chat.username == None:
            send_mes(message, 'Я заметил что у тебя нет юзернейма\n'
                              'Так конечно тоже можно, но человек не сможет выйти'
                              ' на твой аккаунт пока ты не напишешь ему')
            bot.send_message(message.chat.id, 'Продолжим так или ты всё же создашь юзернейм?',
                             reply_markup=bot_types.create_username)

            bot.register_next_step_handler(message, not_username)
            username = False
        else:
            username = True

        if username:
            bot.register_next_step_handler(message, start_reg)


def not_username(message):
    if is_text(message):
        ans = message.text.lower()
        if ans == 'продолжить без него':
            send_mes(message, bot_phrases.username_random())
        elif ans == 'сейчас создам':
            send_mes(message, 'Окей, как закончишь, отправляй /start чтобы зарегистрировать себя')
        else:
            bot.send_message(message.chat.id, 'Прости, я не понял тебя. Ответь на вопрос',
                             reply_markup=bot_types.create_username)
            bot.register_next_step_handler(message, not_username)



def start_reg(message):
    if message.text == bot_types.yesno[1]:
        bot.send_message(message.chat.id, bot_phrases.start_reg_random())
        bot.register_next_step_handler(message, name)
    elif message.text == bot_types.yesno[0]:
        bot.send_message(message.chat.id, bot_phrases.sad_random())
    else:
        send_mes(message, bot_phrases.error_random())
        bot.send_message(message.chat.id, 'Мне регистрировать тебя?', reply_markup=bot_types.askyesno)
        bot.register_next_step_handler(message, start_reg)


def name(message):
    if is_text(message):
        send_mes(message, bot_phrases.age_random())
        user_name = message.text
        bot.register_next_step_handler(message, age, user_name)
    else:
        send_mes(message, bot_phrases.error_random())
        bot.register_next_step_handler(message, name)


def age(message, user_name):
    if is_text(message):
        try:
            user_age = int(message.text)
            bot.send_message(message.chat.id, bot_phrases.loc_random(), reply_markup=bot_types.city)
            bot.register_next_step_handler(message, location, user_age, user_name)

        except Exception as e:
            send_mes(message, 'Цифрами пожалуйста')
            print(f"Age error {e}")
            bot.register_next_step_handler(message, age, user_name)

    else:
        send_mes(message, bot_phrases.error_random())
        send_mes(message, 'Цифрами пожалуйста')
        bot.register_next_step_handler(message, age, user_name)


def location(message, user_age, user_name):
    if is_text(message):
        user_location = message.text
        if user_location.lower() == 'ташкент':
            bot.send_message(message.chat.id, bot_phrases.sex_random(), reply_markup=bot_types.askgender)
            bot.register_next_step_handler(message, user_sex, user_age, user_name, user_location)
        else:
            send_mes(message, 'Увы, этот город пока не поддерживается, я работаю только в Ташкенте ')
            send_mes(message, 'Мхахахаха')
    else:
        send_mes(message, bot_phrases.error_random())


def user_sex(message, user_age, user_name, user_location):
    if is_text(message):
        user_sex_ans = message.text
        check = ['я парень', 'я девушка']

        if user_sex_ans.lower() in check:
            bot.send_message(message.chat.id, bot_phrases.sex_search_random(), reply_markup=bot_types.askgendersearch)
            bot.register_next_step_handler(message, sex_search, user_age, user_name, user_location, user_sex_ans)
        else:
            send_mes(message, bot_phrases.error_random())
            bot.send_message(message.chat.id, 'Ещё раз спрашиваю, кто ты?')
            bot.register_next_step_handler(message, user_sex, user_age, user_name, user_location)
    else:
        send_mes(message, bot_phrases.error_random())
        bot.register_next_step_handler(message, user_sex, user_age, user_name, user_location)


def sex_search(message, user_age, user_name, user_location, user_sex):
    if is_text(message):
        check = ['парней', 'девушек']
        user_sex_search = message.text
        if user_sex_search.lower() in check:
            send_mes(message, bot_phrases.description_random())
            bot.register_next_step_handler(message, description, user_age, user_name, user_location, user_sex,
                                           user_sex_search)
        else:
            bot.send_message(message.chat.id, "Так а кого искать то?", reply_markup=bot_types.askgendersearch)
            bot.register_next_step_handler(message, sex_search, user_age, user_name, user_location, user_sex)
    else:
        send_mes(message, bot_phrases.error_random())


def description(message, user_age, user_name, user_location, user_sex, user_sex_search):
    if is_text(message):
        user_description = message.text
        send_mes(message, 'Так и запишем')
        send_mes(message, bot_phrases.photo_random())
        bot.register_next_step_handler(message, profile_photo, user_age, user_name, user_location, user_sex,
                                       user_sex_search, user_description)
    else:
        send_mes(message, bot_phrases.error_random())


def profile_photo(message, user_age, user_name, user_location, user_sex, user_sex_search, user_description):
    chat_id = message.chat.id

    try:
        username = message.chat.username
    except Exception as e:
        username = 'no_user'
        print(f'No username error {e}')

    try:
        photo = message.photo[-1].file_id

        db_manage.insert(user_name, user_sex, user_age, user_sex_search, user_description,
                         user_location, chat_id, username, photo)
        db_manage.likes_db(chat_id)

        end_registration(message)
    except Exception as e:
        print(e)
        send_mes(message, 'Фотокарточку говорю кидай')
        bot.register_next_step_handler(message, profile_photo, user_age, user_name, user_location, user_sex,
                                       user_sex_search, user_description)


def end_registration(message):
    send_mes(message, bot_phrases.end_reg_random())
    user =  db_manage.select_by_id(message.chat.id)
    bot.send_photo(message.chat.id, user['photo'], caption=f'{user["name"]}, {user["age"]}, {user["city"]}\n\n'
                                                           f'{user["description"]}')


@bot.message_handler(commands=['search'])
def user_search(message, first=True, rec_user_id = ''):
    chat_id = message.chat.id
    print(message.chat)
    try:
        is_text(message)
    except Exception as e:
        print(e)
        send_mes(message, bot_phrases.error_random())
        bot.register_next_step_handler(message, user_search)

    if db_manage.is_exist(chat_id):
        check = ['/search', 'дальше']
        if first or message.text.lower() in check:

            current_user = db_manage.select_by_id(chat_id)
            recommend_user = db_manage.select_man(current_user['sex_search'], current_user['city'], current_user['age'])

            if recommend_user['chat_id'] == 'is_bot':
                photo = open(recommend_user['photo'], 'rb')
                send_mes(message, 'Это бот если что')

            else:
                db_manage.insert_watch(current_user['chat_id'], recommend_user['chat_id'])
                photo = recommend_user['photo']

            opened = False


            bot.send_photo(chat_id, photo, caption=f'{recommend_user["name"]}, {recommend_user["age"]},'
                                                   f' {recommend_user["city"]} \n \n'
                                                   f'{recommend_user["description"]}', reply_markup=bot_types.next)

            if opened:
                photo.close()


            bot.register_next_step_handler(message, user_search, first=False, rec_user_id=recommend_user['chat_id'])

        elif message.text.lower() == 'стоп':
            send_mes(message, "Стою")

        elif message.text.lower() == 'Лайк':
            send_mes(message, "Стою")

        elif message.text.lower() == 'написать':
            print('Рек:', rec_user_id)
            if str(rec_user_id) == str(message.chat.id):
                    send_mes(message, 'Писать самому себе? Гениально!')
            send_mes(message, 'Какое сообщение отправить?')
            bot.register_next_step_handler(message, write_mes, rec_user_id)
        else:
            pass

    else:
        send_mes(message, "Ты не зарегистрирован у нас чтобы искать кого либо")
        send_mes(message, "Отправь /start чтобы зарегистрировать себя")


def write_mes(message, rec_user_id):
    man = db_manage.select_by_id(message.chat.id)
    if is_text(message):
        bot.send_photo(rec_user_id, man['photo'], caption=f'Тебе кто-то написал! <a href="https://t.me/'
                                                          f'{man["username"]}">{man["name"]}</a>: \n'
                                      f'Сообщение: {message.text}', parse_mode='HTML')
        bot.send_sticker(message.chat.id, bot_phrases.send_sticker())
        bot.send_message(message.chat.id, 'Отправил')


@bot.message_handler(content_types=['text'])
def text_response(message):
    send_mes(message, 'testing')
    send_mes(message, '/start \n'
                      '/search \n'
                      '/my_acc \n')


while True:
    try:
        print('Bot started')
        bot.polling(none_stop=True)
    except Exception as error:
        print(f'Bot is crashed: {error}, restart')
        time.sleep(2)
