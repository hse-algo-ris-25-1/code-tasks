def expected_value(i: int, j: int, a: int, b: int, c: int) -> int:
    if i == j:
        return a
    if j == i + 1:
        return b
    if i == j + 1:
        return c
    return 0


def validate_matrix(matrix: list[list[int]]) -> None:
    if not isinstance(matrix, list) or matrix == []:
        raise Exception("Матрица должна быть непустым списком")

    n = len(matrix)
    for row in matrix:
        if not isinstance(row, list) or len(row) != n:
            raise Exception("Матрица должна быть квадратной")
        for value in row:
            if type(value) is not int:
                raise Exception("Все элементы матрицы должны быть целыми")

    a = matrix[0][0]
    b = matrix[0][1] if n > 1 else 0
    c = matrix[1][0] if n > 1 else 0
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != expected_value(i, j, a, b, c):
                raise Exception("Некорректная трёхдиагональная матрица")


def get_tridiagonal_determinant(matrix: list[list[int]]) -> int:
    """Рекурсивное вычисление определителя трёхдиагональной матрицы разложением.

    :param matrix: квадратная целочисленная трёхдиагональная матрица
        порядка не меньше 1 с постоянными значениями на каждой
        из трёх диагоналей
    :raises Exception: если matrix не является такой матрицей
    :return: значение определителя
    """
    validate_matrix(matrix)

    n = len(matrix)
    a = matrix[0][0]
    if n == 1:
        return a  # 2

    b = matrix[0][1]  # -3
    c = matrix[1][0]  # 5

    memo = {0: 1, 1: a}

    def det(k: int) -> int:
        if k in memo:
            return memo[k]
        memo[k] = a * det(k - 1) - b * c * det(k - 2)
        return memo[k]

    return det(n)


def main():
    matrix = [[2, -3, 0, 0], [5, 2, -3, 0], [0, 5, 2, -3], [0, 0, 5, 2]]
    print("Трехдиагональная матрица")
    for row in matrix:
        print(row)

    print(f"Определитель матрицы равен {get_tridiagonal_determinant(matrix)}")


if __name__ == "__main__":
    main()
