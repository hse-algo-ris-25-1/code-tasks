def calculate_determinant(matrix: list[list[int]]) -> int:
    if len(matrix) != len(matrix[0]): raise Exception('Не квадратная матрица')
    if len(matrix) == 1: return matrix[0][0]
    result = 0
    sign = 1
    for i in range(len(matrix[0])):
        result += sign * matrix[0][i] * calculate_determinant(cut_matrix(matrix, i))
        sign *= -1
    return result

def cut_matrix(matrix, column):
    new_matrix = []
    for i in range(1, len(matrix)):
        new_matrix.append([matrix[i][j] for j in range(len(matrix[0])) if j != column])
    return new_matrix

def main():
    matrix = [[1, 2], [3, 4]]
    print("Матрица")
    for row in matrix:
        print(row)

    print(f"Определитель матрицы равен {calculate_determinant(matrix)}")


if __name__ == "__main__":
    main()
