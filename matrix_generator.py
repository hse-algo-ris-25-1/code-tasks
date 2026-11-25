from collections import namedtuple
from random import randint

Case = namedtuple("Case", ["matrix", "det"])

ONLY_3DIAG = True

DETERMINANT = 5
MAX_MULTIPLIER = 1

MAX_VALUE = 5
SQRT_DETERMINANT = 3

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


def mult_matrix(up: list[list[int]], down: list[list[int]]) -> list[list[int]]:
    """
    Умножает матрицы (без разницы какие) up @ down
    :param up: Матрица с главной диагональю + над ней
    :param down: Матрица с главной диагональю + под ней
    """
    n = len(up)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            s = 0
            for p in range(n):
                s += up[i][p] * down[p][j]
            result[i][j] = s
    return result


def generator_3diag(n: int, sqrt_det: int) -> list[list[int]]:
    """
    Генерирует случайную трехдиагональную матрицу порядка n с заданным детерминантом
    :param n: Порядок матрицы
    :param sqrt_det: Корень целевого детерминанта
    :return: matrix
    """
    up = []
    for _ in range(n):
        up.append([0] * n)
    for i in range(n):
        up[i][i] = 1
    up[0][0] = sqrt_det
    down = [row[:] for row in up]

    for i in range(n-1):
        value = randint(-1 * MAX_VALUE, MAX_VALUE) # рандомное значение
        up[i][i+1] = value

    for i in range(1, n):
        value = randint(-1 * MAX_VALUE, MAX_VALUE) # рандомное значение
        down[i][i-1] = value

    return mult_matrix(up, down)

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
    if ONLY_3DIAG:
        matrix = generator_3diag(order, SQRT_DETERMINANT)
        return Case(matrix=matrix, det=DETERMINANT**2)
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