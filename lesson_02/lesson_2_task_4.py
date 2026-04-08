# Задачка с собеседования: FizzBuzz


def fizz_buzz(n):
    """Печатает числа от 1 до n с заменами Fizz, Buzz, FizzBuzz."""
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


# Пример вызова
fizz_buzz(17)