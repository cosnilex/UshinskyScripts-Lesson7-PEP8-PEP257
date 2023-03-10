#!/usr/bin/python3


def fibonacci(n):
    """Нахождение числа Фибоначчи

    Принимает:
        n - число (номер позиции искомого числа Фибоначчи)
    Возвращает:
        Искомое число Фибоначчи
    """
    # Первые два числа Фибоначчи 0 и 1:
    if (n <= 1):
        return n
    else:
        # Каждое следующее число равно сумме двух предыдущих:
        return (fibonacci(n-1) + fibonacci(n-2))


try:
    n = int(f'{input("Введите число: ")}')
except ValueError:
    print(f'Вы ввели не число')
try:
    print(f'Ваше число Фибоначчи: {fibonacci(n)}')
except NameError:
    print(f'Неправильный ввод, либо на ввод ничего не поступило')
