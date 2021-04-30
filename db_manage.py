import sqlite3
import random
import os

def create_db():
    try:
        sqlite_connection = sqlite3.connect('users.db')

        sqlite_create_table_query = '''CREATE TABLE Users (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                    name TEXT NOT NULL,
                                    sex TEXT NOT NULL,
                                    age INTEGER,
                                    sex_search TEXT NOT NULL,
                                    description TEXT NOT NULL,
                                    city TEXT NOT NULL,
                                    fraction TEXT NOT NULL,
                                    voice_message TEXT NOT NULL,
                                    video_message TEXT NOT NULL,
                                    chat_id TEXT NOT NULL,
                                    liked_count INTEGER,
                                    watch_count INTEGER,
                                    user_name TEXT NOT NULL,
                                    photo TEXT NOT NULL);'''

        cursor = sqlite_connection.cursor()

        cursor.execute(sqlite_create_table_query)

        sqlite_create_table_query = '''CREATE TABLE Watched (
                                            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                            first_user_id TEXT NOT NULL,
                                            twice_user_id TEXT NOT NULL,
                                            contacted TEXT NOT NULL
                                            );'''
        cursor.execute(sqlite_create_table_query)

        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)


def age_range(age1):
    range_age1 = [age1 + 1, age1, age1 - 1]
    return range_age1


def insert(name, sex, age, sex_search, description, city, chat_id, username, photo, fraction='Null',
           voice_message='Null',
           video_message='Null'):
    sqlite_connection = None  # just for ide did not swear
    try:
        sqlite_connection = sqlite3.connect('users.db')
        cursor = sqlite_connection.cursor()

        sqlite_insert_query = f"""INSERT INTO Users
                              (name, sex, age, sex_search, description, city, fraction, voice_message,
                              video_message, chat_id, user_name, photo)
                              VALUES
                              ('{name}', '{sex}', '{age}', '{sex_search}', '{description}', '{city}', '{fraction}',
                               '{voice_message}', '{video_message}', '{chat_id}', '{username}', '{photo}');"""
        cursor.execute(sqlite_insert_query)
        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
        print('Внёс')


def age_compatible(age1, age2):
    a = [age1 + 1, age1, age1 - 1]
    b = [age2 + 1, age2, age2 - 1]

    for i in a:
        for j in b:
            if i == j:
                return True


def select_man(sex_search, location, age, random=False, all_gender=False, fraction='default'):
    try:
        sqlite_connection = sqlite3.connect('users.db')
        cursor = sqlite_connection.cursor()
        age = age_range(age)

        if random:
            qry = f""" SELECT * FROM Users ORDER BY RANDOM() LIMIT 1; """

        else:
            if sex_search.lower() == 'парней':
                qry = f""" SELECT * FROM Users WHERE sex = 'Я парень' AND city = '{location}'
                 AND age IN (?,?,?) ORDER BY RANDOM() LIMIT 1; """

            elif sex_search.lower() == 'девушек':
                qry = f""" SELECT * FROM Users WHERE sex = 'Я девушка' AND city = '{location}'
                 AND age IN (?,?,?) ORDER BY RANDOM() LIMIT 1; """

            else:
                qry = f""" SELECT * FROM Users ORDER BY RANDOM() LIMIT 1; """  # very nyeh

        cursor.execute(qry, age)

        records = cursor.fetchall()
        print(records)

        result = {'name': records[0][1],
                  'age': records[0][3],
                  'city': records[0][6],
                  'sex': records[0][2],
                  'sex_search': records[0][4],
                  'description': records[0][5],
                  'fraction': records[0][7],
                  'photo': records[0][14],
                  'chat_id': records[0][10],
                  'username': records[0][13],
                  }

        return result

    except Exception as e:
        print(e)


def insert_fraction(user_tg, fraction):
    sqlite_connection = None  # just for ide did not swear
    try:
        sqlite_connection = sqlite3.connect('users.db')
        cursor = sqlite_connection.cursor()

        sqlite_insert_query = f"""UPDATE Users SET fraction = '{fraction}' WHERE chat_id = {user_tg};"""
        cursor.execute(sqlite_insert_query)
        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
        print('Внёс')


def likes_db(user): # регает юзера в бд по просмотрам
    try:
        sqlite_connection = sqlite3.connect('user_likes.db')
        sqlite_create_table_query = f'''CREATE TABLE IF NOT EXISTS '_{user}_' (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                    liked_user_id TEXT NOT NULL,
                                    pole TEXT);'''

        cursor = sqlite_connection.cursor()
        cursor.execute(sqlite_create_table_query)
        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)


def insert_watch(user1, user2): # voidная функция, суёт просмотренного юзера в таблицу юзера
    sqlite_connection = sqlite3.connect('user_likes.db')
    sqlite_create_table_query = f'''INSERT INTO _{user1}_ (liked_user_id)
                                VALUES
                                ('{user2}');'''

    cursor = sqlite_connection.cursor()
    cursor.execute(sqlite_create_table_query)
    sqlite_connection.commit()
    cursor.close()


def is_watched(user_1, watched_user): # видел ли юзер 1, юзер 2
    sqlite_connection = sqlite3.connect('user_likes.db')
    cursor = sqlite_connection.cursor()

    sqlite_insert_query = f"""SELECT * FROM '_{user_1}_' WHERE liked_user_id = '{watched_user}';"""

    try:
        cursor.execute(sqlite_insert_query)
        sqlite_connection.commit()
        rows = cursor.fetchall()

    except Exception as e:
        print(e)
        return False

    if not rows:
        return False
    else:
        return True


def select_by_id(chat_id): # селект по тг_ид, возвращает словарь с данными о юзере
    sqlite_connection = None  # just for ide did not swear
    try:
        sqlite_connection = sqlite3.connect('users.db')
        cursor = sqlite_connection.cursor()

        sqlite_insert_query = f""" SELECT * FROM Users WHERE `chat_id` = '{chat_id}'; """
        cursor.execute(sqlite_insert_query)

        records = cursor.fetchall()

        result = {'name': records[0][1],
                  'age': records[0][3],
                  'city': records[0][6],
                  'sex': records[0][2],
                  'sex_search': records[0][4],
                  'description': records[0][5],
                  'fraction': records[0][7],
                  'photo': records[0][14],
                  'chat_id': records[0][10],
                  'username': records[0][13],
                  }

        return result

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()


# print(select_by_id(321588123)['photo'])

def is_exist(telegram_id):
    conn = sqlite3.connect("users.db")
    cur = conn.cursor()

    cur.execute(f'''SELECT * FROM Users WHERE Chat_id = '{telegram_id}'; ''')

    rows = cur.fetchall()

    if not rows:
        return False
    else:
        return True


def random_pic():
    pic_list = []
    for root, dirs, files in os.walk("random_pic"):
        for filename in files:
            pic_list.append(filename)
    return random.choice(pic_list)


def create_fake(count):
    names = ['Ирина', 'Достон', 'Игорь', 'РАСТВОРИТЕЛЬ', 'Никита', 'Jahon', 'Гладик', 'ДаНиЛА', 'Айнура',
             'Юля', 'Пеппа', 'Nezuko', 'Kawai-fox, irispro, xuintel']

    descriptions = ['Не можешь сделать женщину счастливой - не мешай другому',
                    'Тот, кто умеет улыбаться каждый день, умеет жить',
                    'Ошибок не делают только спящие.',
                    'Живу на улице, вот это прикол',
                    'Оченб хочу кошкодевочку',
                    'Проблемы заставляют умных людей - действовать, глупых - они вгоняют в депрессию!',
                    'Играю в игры, люблю Ирину',
                    'What if you talking',
                    'А я вот не такой как все',
                    'Я тут видел Никиту, очень бы хотел его найти',
                    'Ищу свободные отношения, люблю разер',
                    'Я фек если че',
                    'ЕэеээЕЭэеэХХ вот бы чичас тяночку',
                    'Ламповая и уютная няшка']

    citys = ['Ташкент', 'Сырдарья']
    sexes = ['Я парень', 'Я девушка']
    sexes_search = ['Девушек', 'Парней']

    a = 0

    while a < count:
        name = random.choice(names)
        age = random.randrange(15, 22)
        description = random.choice(descriptions)
        city = random.choice(citys)
        sex = random.choice(sexes)
        sex_search = random.choice(sexes_search)
        photo = f'random_pic/{random_pic()}'

        insert(name, sex, age, sex_search, description, city, 'is_bot', '@bot', photo)

        a = a + 1

    print(f"{count} fakes created")