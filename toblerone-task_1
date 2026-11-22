from profilehooks import profile


def fibonacci_rec(n: int) -> int:
    if n == 1 or n == 2:
        return 1
    return fibonacci_rec(n-1)+fibonacci_rec(n-2)


def fibonacci_iter(n: int) -> int:
    if n == 1 or n == 2:
        return 1
    m=[0]*(n+1)
    m[0]=0
    m[1]=1
    for i in range(2,n+1):
        m[i] = m[i-1]+m[i-2]
    return m[-1]
print(fibonacci_iter(6))


def fibonacci(n: int) -> int:
    if n == 1 or n == 2:
        return 1
    a=1
    b=1
    c=0
    while n>2:      
        c=a+b
        a=b
        b=c
        n-=1
    return c
print(fibonacci(7))


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
