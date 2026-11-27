#from profilehooks import profile


def fibonacci_rec(n: int) -> int:
    if n <= 2: return 1
    return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)

def fibonacci_iter(n: int) -> int:
    l = [0] * (n + 1)
    l[0] = l[1] = 1
    for i in range(2, n + 1):
        l[i] = l[i-1] + l[i-2]
    return l[n - 1]

def fibonacci(n: int) -> int:
    a = b = c = 1
    for i in range(3, n + 1):
        c = a + b
        a = b
        b = c
    return c


def main():
    n = 35
    print(f"Вычисление {n} числа Фибоначчи рекурсивно:")
    print(fibonacci_rec(n))

    print(f"\nВычисление {n} числа Фибоначчи итеративно:")
    print(fibonacci_iter(n))

    print(f"\nВычисление {n} числа Фибоначчи итеративно без использования массива:")
    print(fibonacci(n))


