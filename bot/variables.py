HELP_MESSAGE = 'Команды бота:\n/play {Число игроков} >> Составить список чисел.\n/number >> Выдача случайного числа из списка чисел игроков.\n/help >> Команды бота.'


SMILE_NUMBERS_LIST = ['0️⃣', '1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣']


def get_smile_number(number: int) -> str:
    smile_number = ''
    for x in str(number):
        smile_number += SMILE_NUMBERS_LIST[int(x)]
    return smile_number
