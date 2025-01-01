"""
Модуль для пользовательских исключений.
"""

class GiftBotError(Exception):
    """
    Базовый класс для всех исключений бота.
    """
    pass

class ValidationError(GiftBotError):
    """
    Исключение, возникающее при ошибке валидации данных.
    """
    pass

class BudgetError(GiftBotError):
    """
    Исключение, возникающее при ошибках, связанных с бюджетом.
    """
    pass

class FileLoadError(GiftBotError):
    """
    Исключение, возникающее при ошибке загрузки файла с подарками.
    """
    pass

class GiftSelectionError(GiftBotError):
    """
    Исключение, возникающее при ошибке подбора подарков.
    """
    pass

class InvalidGiftDataError(GiftBotError):
    """
    Исключение, возникающее при обнаружении некорректных данных в gifts.json.
    """
    pass
