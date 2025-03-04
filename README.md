# Проект Маскировки Номеров

Этот проект реализует функции для маскировки номеров банковских карт и счетов, а также предоставляет возможность фильтрации данных по состоянию.

## Структура проекта

Проект состоит из следующих модулей:

1. **masks**: 
   - `get_mask_card_number(card_number: str) -> str`: Функция для маскировки номера банковской карты. Возвращает замаскированный номер карты.
   - `get_mask_account(account_number: str) -> str`: Функция для маскировки номера банковского счета. Возвращает замаскированный номер счета.

2. **widget**:
   - `mask_account_card(info: str) -> str`: Функция, которая принимает строку, содержащую тип и номер карты или счета, и возвращает строку с замаскированным номером. Использует разные типы маскировки для карт и счетов.

3. **processing**:
   - `filter_by_state(data: list, state: str = 'EXECUTED') -> list`: Функция, которая принимает список словарей и опционально значение для ключа `state`. Возвращает новый список словарей, содержащий только те словари, у которых ключ `state` соответствует указанному значению.
  
## Проверка кода

В проекте выполнены проверки линкерами:
- **Flake8**: для проверки стиля кода.
- **mypy**: для статической типизации.
- **black**: для автоматического форматирования кода.
- **isort**: для сортировки импортов.

## Лицензия

Этот проект лицензирован под MIT License. См. файл [LICENSE](LICENSE) для получения дополнительной информации.
