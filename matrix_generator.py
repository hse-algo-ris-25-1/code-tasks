from collections import namedtuple
from random import randint

Case = namedtuple("Case", ["matrix", "det"])

DETERMINANT = 5
MAX_MULTIPLIER = 1

def add_row(matrix: list[list[int]], origin: int, target: int, multiplier: int = 1) -> None:
    """
    Прибавляет строку origin (умножается на multiplier) к target строке
    :param origin: Исходная строка
    :param target: Целевая строка
    :param multiplier: Мультипликатор исходной строки (по умолчанию = 1)
    """
    n = len(matrix)
    if origin == target or origin > n-1 or target > n-1 or origin < 0 or target < 0:
        return
    for i in range(n):
        matrix[target][i] += matrix[origin][i] * multiplier


def add_column(matrix: list[list[int]], origin: int, target: int, multiplier: int = 1) -> None:
    """
    Прибавляет столбец origin (умножается на multiplier) к target столбцу
    :param origin: Исходная строка
    :param target: Целевая строка
    :param multiplier: Мультипликатор исходной строки (по умолчанию = 1)
    """
    n = len(matrix)
    if origin == target or origin > n-1 or target > n-1 or origin < 0 or target < 0:
        return
    for i in range(n):
        matrix[i][target] += matrix[i][origin] * multiplier

def generator(n: int, det: int) -> list[list[int]]:
    """
    Генерирует случайную матрицу порядка n с заданным детерминантом
    :param n: Порядок матрицы
    :param det: Целевой детерминант
    :return: matrix
    """
    # построение диагональной
    matrix = []
    for _ in range(n):
        matrix.append([0] * n)
    for i in range(n):
        matrix[i][i] = 1
    matrix[0][0] = det

    # n^2 рандомных операций
    for _ in range(n**2):
        direction = randint(0, 1)  # работа со строками или с колонками
        origin = randint(0, n) # откуда берем
        target = randint(0, n) # что изменяем
        multiplier = randint(-1 * MAX_MULTIPLIER, MAX_MULTIPLIER) # на что умножаем
        if direction == 0:
            add_row(matrix, origin, target, multiplier)
        else:
            add_column(matrix, origin, target, multiplier)

    return matrix

def generate_matrix_and_det(order: int) -> Case:
    """Строит квадратную целочисленную матрицу заданного порядка
    с заранее известным определителем.

    Определитель получают из свойств, не вычисляя его разложением
    и не вызывая calculate_determinant.

    :param order: порядок матрицы, целое число не меньше 1
    :raises Exception: если order не является таким числом
    :return: Case с полями matrix и det
    """
    if order < 1:
        raise Exception
    matrix = generator(order, DETERMINANT)
    return Case(matrix=matrix, det=DETERMINANT)

def main():
    n = 10
    print(f"Генерация матрицы порядка {n}")
    result = generate_matrix_and_det(n)
    print("\nОпределитель сгенерированной матрицы равен", result.det)
    print("\n".join(["\t".join([str(cell) for cell in row]) for row in result.matrix]))


if __name__ == "__main__":
    main()