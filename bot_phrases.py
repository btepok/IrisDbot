import random


def hello_sticker():
    hello_sticker = [
        'CAACAgIAAxkBAAEBKaJfLpxqVcylVaDLtu7FGcDmmUiMuAACqQADRpIBL168VNIXoeGiGgQ',
        'CAACAgIAAxkBAAEBR1hfTLs4IwPlvKth1PYp8d_pVEQdwQACWQADIfAEHEef7qP9uC3xGwQ',
        'CAACAgIAAxkBAAEBR2RfTLyAXiHPPhX4wvnl-u0Ls1TTEgACfwADq1fEC0HS9LG5zsfPGwQ',
        'CAACAgIAAxkBAAEBR2hfTMc-ObcmWqgmKKbvmt8GrUwGmQACEwADsND4DBk_m0DRzeuqGwQ',
        'CAACAgIAAxkBAAEBR2xfTMgVeAqab7Vc-_Nk5M_VNlisZAACWAYAAhnydRsO4XTCeBTNJRsE',
        'CAACAgIAAxkBAAEBR3VfTMipSWGUAX291o8h_XApz4JwgwACJwMAArVx2gYP9N7PoMXd7BsE'
    ]

    return random.choice(hello_sticker)


def send_sticker():
    return 'CAACAgIAAxkBAAEGzMlgirjjm445_2TFdzOAGoOoGdqiXQAC2AADVp29CokJ3b9L8RQnHwQ'


def endreg_sticker():
    reg_sticker = [
        'CAACAgIAAxkBAAEGrRhgejbWZhG5sGs1WoNJ5KN-1Iv40wACdxEAAjyzxQdiXqFFBrRFjx8E',
        'CAACAgIAAxkBAAEGrRZgejaFI7yWDc2glNDbhycsfx79SwACygADq1fEC3fQ4RKXbxJiHwQ',
        'CAACAgIAAxkBAAEGrRRgejZuU_qBv1PjtGFAxl02IfAoXAAC5xAAAowt_QehzoA4bWwLCR8E',
        'CAACAgIAAxkBAAEGrRJgejYIi3bsCbX8jph4TITPZhZkZwACRwADa9dMC8cJziF44O-dHwQ',
        'CAACAgIAAxkBAAEGrRpgejdY_NP-oqal_vNqdYz3wRetIwAC9QUAAtCG-wpJ1-fmiM6kPR8E',
        'CAACAgIAAxkBAAEGrRxgejd8TPajg3UxUsVDWO9CFlgsdAACuQADRpIBL9uijIM0_VUJHwQ'
    ]

    return random.choice(reg_sticker)


def hello_random():
    phrases = ['Привет, я бот который поможет найти тебе пару',
               'Привет, надеюсь я смогу найти тебе хорошего друга']
    return random.choice(phrases)


def start_reg_random():
    phrases = ['Ура, давай регистрироваться, пиши своё имя',
               'Хорошо, перейдём к регистрации, как тебя зовут?', ]
    return random.choice(phrases)


def username_random():
    phrases = ['Ну ладно',
               'Хорошо, будь по твоему', ]
    return random.choice(phrases)


def end_reg_random():
    phrases = ['Отлично! Так выглядит твоя анкета:',
               'Спасибо, вот как тебя будут видеть пользователи:']
    return random.choice(phrases)


def error_random():
    phrases = ['Не понял',
               'А чё с этим делать?', ]
    return random.choice(phrases)


def photo_random():
    phrases = ['Кидай свою фотку \n'
               'Или не свою, мне всё равно',
               'Теперь кидай фотокарточку',
               'Скинь любое фото']
    return random.choice(phrases)


def age_random():
    phrases = ['А сколько лет?',
               'А возраст?', ]
    return random.choice(phrases)


def loc_random():
    phrases = ['Где будем искать?',
               'Какой город?', ]
    return random.choice(phrases)


def sex_random():
    phrases = ['Определимся с полом',
               'Какого ты пола?']

    return random.choice(phrases)


def sex_search_random():
    phrases = ['Кого будем искать?',
               'Кого искать?', ]
    return random.choice(phrases)


def description_random():
    phrases = ['Теперь опиши себя',
               'Как ты можешь описать себя?', ]
    return random.choice(phrases)


def sad_random():
    phrases = ['Ну ладно 😒',
               'ме(', ]
    return random.choice(phrases)
