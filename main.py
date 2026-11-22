def calculate_determinant(a: list[list[int]]) -> int:
    """Вычисляет определитель разложением по строке.

    :param matrix: квадратная целочисленная матрица порядка не меньше 1
    :raises Exception: если matrix не является такой матрицей
    :return: значение определителя
    """
    if not a or not a[0]:
        raise ValueError("Матрица пустая")
    n = len(a)
    for row in a:
        if len(row) != n:
            raise ValueError("Матрица не квадратная")
    if n == 1:
        return a[0][0]

    deter = 0
    for i in range(n):
        deter += (a[0][i] * (-1) ** (0 + i + 2)) * calculate_determinant(delete_0_i(a, i))
    return deter

def delete_0_i(a, i):
    b = []
    for k in range(1, len(a)):
        c = []
        for j in range(len(a[k])):
            if j != i:
                c.append(a[k][j])
        b.append(c)
    return b

def main():
    matrix = [[1, 2], [3, 4]]
    print("Матрица")
    for row in matrix:
        print(row)

    print(f"Определитель матрицы равен {calculate_determinant(matrix)}")


if __name__ == "__main__":
    main()
