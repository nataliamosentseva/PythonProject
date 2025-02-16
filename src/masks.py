cadr_number = "7000792289606361"


def get_mask_card_number(card_number: str) -> str | None:

    """Функция принимает на вход номер карты и возвращает ее маску.
    Номер карты замаскирован и отображается в формате XXXX XX** **** XXXX"""
    if card_number.isdigit() and len(card_number) == 16:
        return f"{card_number[:4]} {card_number[4:6]}{"*" * 2} {"*" * 4} {card_number[12:]}"
    else:
        return None


account_number = "73654108430135874305"


def get_mask_account(account_number: str) -> str | None:

    """ Функция принимает на вход номер счета и возвращает его маску.
    Номер счета замаскирован и отображается в формате **XXXX"""
    if account_number.isdigit() and len(account_number) == 20:
        return f"{'*' * 2} {account_number[-4::]}"
    else:
        return None
