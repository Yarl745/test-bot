from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

config_menu = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton("Изменить Имя"),
        ],
        [
            KeyboardButton("Изменить Возраст"),
        ],
        [
            KeyboardButton("Изменить Пол"),
        ],
        [
            KeyboardButton("Назад ↩️")
        ]
    ],
    resize_keyboard=True
)
