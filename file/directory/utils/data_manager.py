"""
Модуль для работы с данными о подарках.
"""

import json
import random
from gift_core.exceptions import FileLoadError, InvalidGiftDataError
from gift_core import validate_gift_data

class DataManager:
    """
    Класс для управления данными о подарках.
    """

    def __init__(self, file_path: str):
        """
        Инициализация менеджера данных.

        :param file_path: Путь к файлу с данными о подарках.
        """
        self.file_path = file_path
        self.gift_data = []

    def load_gift_bank(self):
        """
        Загружает данные о подарках из JSON-файла.

        :raises FileLoadError: Если файл не найден или некорректен.
        :raises InvalidGiftDataError: Если данные в файле имеют неверный формат.
        """
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)

            if not isinstance(data, list):
                raise InvalidGiftDataError("Ожидается список подарков в файле.")

            for item in data:
                validate_gift_data(item)

            self.gift_data = data
        except FileNotFoundError:
            raise FileLoadError(f"Файл {self.file_path} не найден.")
        except json.JSONDecodeError:
            raise FileLoadError(f"Ошибка декодирования JSON в файле {self.file_path}.")

    def get_all_gifts_shuffled(self):
        """
        Возвращает все подарки в случайном порядке.

        :return: Список всех подарков в случайном порядке.
        """
        return random.sample(self.gift_data, len(self.gift_data))
