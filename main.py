from src.widget import get_mask_account, get_mask_card_number, mask_account_card, get_date

print(get_mask_card_number("7000792289606361"))
print(get_mask_account("73654108430135874305"))

if __name__ == "__main__":
    print(mask_account_card("Visa Platinum 8990922113665229"))
    print(mask_account_card("Maestro 1596837868705199"))
    print(mask_account_card("Счет 73654108430135874305"))
    print(get_date("2024-03-11T02:26:18.671407"))
