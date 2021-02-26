from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton("Обезьяньй паспорт 🐒"),
            KeyboardButton("Настройки ⚙️")
        ]
    ],
    resize_keyboard=True
)