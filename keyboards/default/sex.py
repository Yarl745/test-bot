from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_sex(with_back=False):
    sex: ReplyKeyboardMarkup

    keyboard = [
        [
            KeyboardButton("Я мужчина 🙋‍♂️"),
            KeyboardButton("Я женщина 🙋‍♀️")
        ]
    ]

    if with_back:
        keyboard.append([KeyboardButton("Назад ↩️")])

    sex = ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True
    )

    return sex
