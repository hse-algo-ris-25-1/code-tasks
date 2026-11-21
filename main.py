def calculate_determinant(matrix: list[list[int]]) -> int:
    """Вычисляет определитель разложением по строке.

    :param matrix: квадратная целочисленная матрица порядка не меньше 1
    :raises Exception: если matrix не является такой матрицей
    :return: значение определителя
    """
    n = len(matrix)
    if n == 0:
        raise Exception("Матрица пустая")
    for row in matrix:
        if len(row) != n:
            raise Exception("Матрица не квадратная")
        for x in row:
            if type(x) is not int:
                raise Exception("Элементы должны быть целыми числами")

    if n == 1:
        return matrix[0][0]

    # разложение по первой строке
    result = 0
    for j in range(n):
        # минор: убираем первую строку и столбец j
        minor = [row[:j] + row[j + 1 :] for row in matrix[1:]]
        sign = 1 if j % 2 == 0 else -1
        result += sign * matrix[0][j] * calculate_determinant(minor)
    return result


def main():
    matrix = [[1, 2], [3, 4]]
    print("Матрица")
    for row in matrix:
        print(row)

    print(f"Определитель матрицы равен {calculate_determinant(matrix)}")


if __name__ == "__main__":
    main()
