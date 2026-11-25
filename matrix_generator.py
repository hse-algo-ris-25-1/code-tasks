from collections import namedtuple
from random import randint

Case = namedtuple("Case", ["matrix", "det"])

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
        raise Exception("Ошибка! Порядок матрицы должен быть больше или равен 1")
    matrix = []
    if order == 1:
        det = randint(-10, 10)
        matrix.append([det])
        return Case(matrix, det)
    det = 1
    for i in range(order):
        row = []
        for j in range(order):
            if i > j:
                row.append(0)
            else:
                row.append(randint(-10, 10))
        matrix.append(row)
    for i in range(order):
        det *= matrix[i][i]
    for i in range(1, order):
        coefficient = randint(-5, 5)
        if coefficient == 0:
            coefficient = 1
        for j in range(order):
            matrix[i][j] += coefficient * matrix[i - 1][j]
    return Case(matrix, det)


def main():
    n = 10
    print(f"Генерация матрицы порядка {n}")
    result = generate_matrix_and_det(n)
    print("\nОпределитель сгенерированной матрицы равен", result.det)
    print("\n".join(["\t".join([str(cell) for cell in row]) for row in result.matrix]))


if __name__ == "__main__":
    main()
