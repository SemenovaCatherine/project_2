"""
Модуль для создания клавиатур для бота.
"""

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Главное меню
main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Указать бюджет")],
    ],
    resize_keyboard=True
)

# Меню после указания бюджета
budget_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Подобрать подарки")],
        [KeyboardButton(text="Назад")]
    ],
    resize_keyboard=True
)

# Кнопка "Назад"
back_button = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Назад")]
    ],
    resize_keyboard=True
)
