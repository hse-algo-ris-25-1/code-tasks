def calculate_determinant(matrix: list[list[int]]) -> int:
    """Вычисляет определитель разложением по строке.

    :param matrix: квадратная целочисленная матрица порядка не меньше 1
    :raises Exception: если matrix не является такой матрицей
    :return: значение определителя
    """
    if not isinstance(matrix, list):
        raise Exception("Матрица должна быть списком списков")

    if len(matrix) == 0:
        raise Exception("Матрица не может быть пустой")


    n = len(matrix)

    # проверка на квадратность
    for row in matrix:
        if not isinstance(row, list):
            raise Exception("Каждая строка матрицы должна быть списком")
        if len(row) != n:
            raise Exception("Матрица должна быть квадратной")

    # проверка на целые числа
    for row in matrix:
        for value in row:
            if not isinstance(value, int) or isinstance(value, bool):
                raise Exception("Элементы матрицы должны быть целыми числами")

    if n == 0:
        return 1

    if n == 1:
        return matrix[0][0]

    det = 0
    for j in range(n):
        minor = [row[:j] + row[j+1:] for row in matrix[1:]]
        det += matrix[0][j] * calculate_determinant(minor) * ((-1) ** j)

    return det


def main():
    matrix = [[1, 2], [3, 4]]
    print("Матрица")
    for row in matrix:
        print(row)

    print(f"Определитель матрицы равен {calculate_determinant(matrix)}")


if __name__ == "__main__":
    main()
