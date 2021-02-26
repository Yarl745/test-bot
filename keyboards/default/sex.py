from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

sex = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton("Я мужчина 🙋‍♂️"),
            KeyboardButton("Я женщина 🙋‍♀️")
        ]
    ],
    resize_keyboard=True
)