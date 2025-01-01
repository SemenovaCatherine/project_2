"""
Модуль для описания состояний FSMContext.
"""

from aiogram.fsm.state import State, StatesGroup

class GiftBotStates(StatesGroup):
    """
    Состояния для взаимодействия с ботом.
    """
    waiting_for_budget = State()
    waiting_for_action = State()
