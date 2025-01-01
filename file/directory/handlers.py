"""
Модуль для обработки команд и сообщений бота.
"""

import os
from aiogram import types, Router
from aiogram.fsm.context import FSMContext
from aiogram.filters.command import Command
from aiogram.filters.state import StateFilter
from telegram_bot.keyboards import main_menu, budget_menu, back_button
from telegram_bot.states import GiftBotStates
from gift_core.data_manager import DataManager
from gift_core.budget_manager import BudgetManager
from gift_core.exceptions import BudgetError

# Создаём роутер
router = Router()

# Определяем путь к gifts.json относительно корня проекта
gifts_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "gifts.json")

@router.message(Command(commands=["start"]))
async def start_command(message: types.Message):
    """
    Обработка команды /start. Отправляет приветствие и главное меню.
    """
    await message.answer(
        "Привет! Я помогу подобрать подарки на Новый Год 🎄\nВыберите действие:",
        reply_markup=main_menu
    )

@router.message(lambda message: message.text == "Указать бюджет")
async def ask_for_budget(message: types.Message, state: FSMContext):
    """
    Обработка выбора "Указать бюджет". Переводит пользователя в состояние ожидания ввода бюджета.
    """
    await message.answer("Введите сумму бюджета:", reply_markup=back_button)
    await state.set_state(GiftBotStates.waiting_for_budget)

@router.message(StateFilter(GiftBotStates.waiting_for_budget))
async def set_budget(message: types.Message, state: FSMContext):
    """
    Обработка ввода бюджета. Сохраняет бюджет и предлагает действия.
    """
    try:
        budget = float(message.text)
        if budget <= 0:
            raise ValueError
    except ValueError:
        await message.answer("Пожалуйста, введите положительное число.", reply_markup=back_button)
        return

    await state.update_data(budget=budget)
    await message.answer(
        f"Ваш бюджет: {budget:.2f} руб.\nЧто дальше?",
        reply_markup=budget_menu
    )
    await state.set_state(GiftBotStates.waiting_for_action)

@router.message(lambda message: message.text == "Подобрать подарки", StateFilter(GiftBotStates.waiting_for_action))
async def get_gifts(message: types.Message, state: FSMContext):
    """
    Подбирает подарки на основе текущего бюджета пользователя.
    """
    user_data = await state.get_data()
    budget = user_data.get("budget")

    try:
        # Загрузка данных и подбор подарков
        data_manager = DataManager(gifts_file_path)
        data_manager.load_gift_bank()
        budget_manager = BudgetManager(budget)
        gifts, remaining = budget_manager.select_gifts_within_budget(data_manager.get_all_gifts_shuffled())

        # Формирование ответа
        response = "🎁 Подобраны следующие подарки:\n"
        for gift in gifts:
            response += f"  - {gift['name']} ({gift['price']} руб.)\n"
        response += f"\nОстаток бюджета: {remaining:.2f} руб."

        await message.answer(response, reply_markup=budget_menu)

    except BudgetError:
        await message.answer("❌ Не удалось подобрать подарки. Попробуйте изменить бюджет.", reply_markup=budget_menu)

@router.message(lambda message: message.text == "Назад")
async def go_back(message: types.Message, state: FSMContext):
    """
    Обработка кнопки "Назад". Возвращает в главное меню.
    """
    await state.clear()
    await message.answer("Выберите действие:", reply_markup=main_menu)
