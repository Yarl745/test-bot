from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton("Обезьяний паспорт 🐒"),
            KeyboardButton("Настройки ⚙️")
        ]
    ],
    resize_keyboard=True
)