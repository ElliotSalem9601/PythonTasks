# Площадь квадрата

import math


def square(side):
    """
    Возвращает площадь квадрата.
    Если side не целое, результат округляется вверх.
    """
    area = side * side
    return math.ceil(area)


# Проверка (можно закомментировать или удалить)
print(square(5))    # 25
print(square(2.5))  # 6.25 -> 7