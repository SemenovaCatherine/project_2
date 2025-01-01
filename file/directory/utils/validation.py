"""
Модуль для валидации данных.
"""

from gift_core import ValidationError

def validate_budget(budget):
    """
    Проверяет, что бюджет является положительным числом.

    :param budget: Значение бюджета для проверки.
    :raises ValidationError: Если бюджет некорректен.
    """
    if not isinstance(budget, (int, float)) or budget <= 0:
        raise ValidationError("Бюджет должен быть положительным числом.")

def validate_gift_data(gift):
    """
    Проверяет, что данные подарка имеют корректную структуру.

    :param gift: Словарь с данными подарка.
    :raises ValidationError: Если структура данных некорректна.
    """
    if not isinstance(gift, dict):
        raise ValidationError("Подарок должен быть представлен в виде словаря.")

    if not isinstance(gift.get('name'), str):
        raise ValidationError("Поле 'name' должно быть строкой.")

    if not isinstance(gift.get('price'), (int, float)) or gift['price'] < 0:
        raise ValidationError("Поле 'price' должно быть положительным числом.")

    if not isinstance(gift.get('category'), str):
        raise ValidationError("Поле 'category' должно быть строкой.")
