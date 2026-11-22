def fibonacci_rec(n: int) -> int:
    if n <= 0:
        return 0
    if n in (1, 2):
        return 1
    return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)


def fibonacci_iter(n: int) -> int:
    fib = [0] * (n + 1)
    fib[1] = 1
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib[n]


def fibonacci(n: int) -> int:
    if n <= 0:
        return 0
    if n == 1:
        return 1
    past = 1
    overpast = 0
    for i in range(2, n + 1):
        curr = past + overpast
        overpast = past
        past = curr
    return past


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
