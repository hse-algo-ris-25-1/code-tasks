def calculate_determinant(matrix: list[list[int]]) -> int:
    if not matrix:
        raise ValueError("Матрица не может быть пустой")

    n = len(matrix)
    if any(len(row) != n for row in matrix):
        raise ValueError("Матрица должна быть квадратной")

    if n == 1:
        return matrix[0][0]
    det = 0
    for c in range(n):
        minor = [row[:c] + row[c + 1 :] for row in matrix[1:]]
        det += (-1) ** c * matrix[0][c] * calculate_determinant(minor)
    return det


def main():
    matrix = [[1, 2], [3, 4]]
    print("Матрица")
    for row in matrix:
        print(row)

    print(f"Определитель матрицы равен {calculate_determinant(matrix)}")


if __name__ == "__main__":
    main()
