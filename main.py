def calculate_determinant(matrix: list[list[int]]) -> int:
    """Вычисляет определитель разложением по строке.

    :param matrix: квадратная целочисленная матрица порядка не меньше 1
    :raises Exception: если matrix не является такой матрицей
    :return: значение определителя
    """
    n = len(matrix)
    if n == 0:
        raise Exception("Пустая матрица")
    for row in matrix:
        if len(row)  is not n:
            raise Exception("Матрица не является квадратной")
        for element in row:
            if type(element)  is not int:
                raise Exception("Матрица должна состоять из целых чисел")
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    determinant = 0
    for column in range(n):
        minor = [row[:column] + row[column + 1 :] for row in matrix[1:]]
        minor_det = calculate_determinant(minor)
        sign = (-1) ** column
        determinant += sign * matrix[0][column] * minor_det
    return determinant


def main():
    matrix = [[1, 2], [3, 4]]
    print("Матрица")
    for row in matrix:
        print(row)

    print(f"Определитель матрицы равен {calculate_determinant(matrix)}")


if __name__ == "__main__":
    main()
