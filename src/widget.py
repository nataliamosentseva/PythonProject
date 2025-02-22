from src.masks import get_mask_card_number, get_mask_account
from datetime import datetime


def mask_account_card(name_card_account: str) -> str:
    """Функция, которая умеет обрабатывать информацию как о картах,
    так и о счетах."""
    if "Счет" in name_card_account:
        number = name_card_account.replace("Счет", "").strip()
        return "Счет " + get_mask_account(number)

    else:
        numbers = get_mask_card_number(name_card_account[-16:])
        new_number = " ".join(name_card_account.split()[:-1]) + " " + numbers
        return new_number


def get_date(date_str: str) -> str:
    """Функция, которая принимает на вход строку с датой в формате
    "2024-03-11T02:26:18.671407"
    и возвращает строку с датой в формате "ДД.ММ.ГГГГ"("11.03.2024")."""
    dt = datetime.fromisoformat(date_str)
    return dt.strftime("%d .%m .%Y")


if __name__ == "__main__":
    print(mask_account_card("Visa Platinum 8990922113665229"))
    print(mask_account_card("Maestro 1596837868705199"))
    print(mask_account_card("Счет 73654108430135874305"))
    print(get_date("2024-03-11T02:26:18.671407"))
