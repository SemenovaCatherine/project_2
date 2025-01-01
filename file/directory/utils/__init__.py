"""
Инициализация пакета gift_core. Предоставляет основные классы и функции.
"""

from .exceptions import BudgetError, ValidationError
from .validation import validate_budget, validate_gift_data
from .budget_manager import BudgetManager

__all__ = [
    "BudgetError",
    "ValidationError",
    "validate_budget",
    "validate_gift_data",
    "BudgetManager",
]
