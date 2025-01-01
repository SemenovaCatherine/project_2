"""
Модуль для управления бюджетом и подбора подарков.
"""

from gift_core.exceptions import BudgetError

class BudgetManager:
    def __init__(self, budget):
        """
        Инициализирует менеджер бюджета.

        :param budget: Бюджет пользователя.
        """
        self.budget = budget

    def select_gifts_within_budget(self, gifts):
        """
        Подбирает подарки, которые укладываются в бюджет.
        Возвращает список выбранных подарков и остаток бюджета.

        :param gifts: Список доступных подарков.
        :return: Кортеж (список подарков, остаток бюджета).
        :raises BudgetError: Если невозможно подобрать подарки в пределах бюджета.
        """
        selected_gifts = []
        total_cost = 0
        remaining_budget = self.budget  # Инициализация остатка бюджета

        for gift in gifts:
            if gift['price'] <= remaining_budget:
                selected_gifts.append(gift)
                total_cost += gift['price']
                remaining_budget -= gift['price']  # Обновляем остаток бюджета

        if not selected_gifts:
            raise BudgetError("Невозможно подобрать подарки в пределах бюджета.")

        return selected_gifts, remaining_budget
