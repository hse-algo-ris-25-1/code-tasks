from profilehooks import profile


def fibonacci_rec(n: int) -> int:
    if n ==0:
        return 0
    if n == 1 or n == 2:
        return 1
    if n > 2:
        return fibonacci_rec(n-1) + fibonacci_rec(n-2)
    
    """Возвращает N-е число Фибоначчи. Реализована рекурсивно согласно
    формуле вычисления последовательности.
    
    :param n: порядковый номер числа Фибоначчи
    :return: число Фибоначчи
    """
    pass


def fibonacci_iter(n: int) -> int:
    a = [1] * n
    for i in range(2, n):
        a[i] = a[i-1] + a[i-2]
    return a[-1]
    """Возвращает N-е число Фибоначчи. Реализована итеративно с использованием
    массива для хранения вычисляемых данных.

    :param n: порядковый номер числа Фибоначчи
    :return: число Фибоначчи
    """
    pass


def fibonacci(n: int) -> int:
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a
    """Возвращает N-е число Фибоначчи. Реализована итеративно без использования массива.

    :param n: порядковый номер числа Фибоначчи
    :return: число Фибоначчи
    """
    pass


def main():
    n = 35
    print(f"Вычисление {n} числа Фибоначчи рекурсивно:")
    print(fibonacci_rec(n))

    print(f"\nВычисление {n} числа Фибоначчи итеративно:")
    print(fibonacci_iter(n))

    print(f"\nВычисление {n} числа Фибоначчи итеративно без использования массива:")
    print(fibonacci(n))


if __name__ == "__main__":
    main()
