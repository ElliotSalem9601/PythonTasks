# Месяц — сезон


def month_to_season(month):
    """
    Возвращает название сезона по номеру месяца.
    month: int от 1 до 12.
    """
    if month in (12, 1, 2):
        return "Зима"
    elif month in (3, 4, 5):
        return "Весна"
    elif month in (6, 7, 8):
        return "Лето"
    elif month in (9, 10, 11):
        return "Осень"
    else:
        return "Неверный номер месяца"


# Проверка (пример)
print(month_to_season(2))   # Зима
print(month_to_season(5))   # Весна