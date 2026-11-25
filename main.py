import sys

sys.stdout.reconfigure(encoding="utf-8")


# Проверка начальной матрицы на корректность и вызов вычисляющей функции
def get_tridiagonal_determinant(matrix: list[list[int]]) -> int:
    """Рекурсивное вычисление определителя трёхдиагональной матрицы разложением.

    :param matrix: квадратная целочисленная трёхдиагональная матрица
        порядка не меньше 1 с постоянными значениями на каждой
        из трёх диагоналей
    :raises Exception: если matrix не является такой матрицей
    :return: значение определителя
    """

    if not isinstance(matrix, list) or len(matrix) == 0: # Если матрица не является списком или пустая
        raise Exception
    
    if any(not isinstance(row, list) for row in matrix): # Если хотя бы одна строка матрицы не является списком
        raise Exception

    n = len(matrix)
    if any(len(row) != n for row in matrix) or any( # Если матрица не квадратная или
        matrix[i][j] != 0
        for i in range(n)
        for j in range(n)
        if abs(i - j) > 1 # вне диагоналей есть ненулевой элемент
    ):
        raise Exception

    if any(
        type(x) is not int for row in matrix for x in row
    ):  # Если матрица не целочисленная
        raise Exception

    if n > 1:  # Если в матрице невырожденне диагонали
        mid = matrix[0][0]  # Главная диагональ
        right = matrix[0][1]  # Верхняя диагональ
        left = matrix[1][0]  # Нижняя диагональ

        for i in range(n):  # По всей матрице
            if matrix[i][i] != mid:
                raise Exception

            if i < n - 1:
                if matrix[i][i + 1] != right:
                    raise Exception
                if matrix[i + 1][i] != left:
                    raise Exception

    return calculate_recursive(matrix)


# Вычисление определителя для УЖЕ корректной матрицы
def calculate_recursive(matrix: list[list[int]]) -> int:
    n = len(matrix)

    if n == 1:
        return matrix[0][0]
    if n == 0:
        return 1

    return matrix[0][0] * calculate_recursive(
        [row[1 : n + 1] for row in matrix[1 : n + 1]]
    ) - matrix[0][1] * matrix[1][0] * calculate_recursive(
        [row[2 : n + 1] for row in matrix[2 : n + 1]]
    )


def main():
    matrix = [[2, -3, 0, 0], [5, 2, -3, 0], [0, 5, 2, -3], [0, 0, 5, 2]]
    print("Трехдиагональная матрица")
    for row in matrix:
        print(row)

    print(f"Определитель матрицы равен {get_tridiagonal_determinant(matrix)}")


if __name__ == "__main__":
    main()
