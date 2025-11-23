def float_if_needed(x):
    if '.' in x:
        return float(x)
    return int(x)


def read_matrix_with_size():
    n, m = map(int, input().split())
    matrix = []
    for _ in range(n):
        row = list(map(float_if_needed, input().split()))
        matrix.append(row)
    return matrix, n, m


def print_matrix(matrix):
    for row in matrix:
        print(*row)


def add_matrices():
    print('Enter size of first matrix:', end=' ')
    matrix1, n1, m1 = read_matrix_with_size()

    print('Enter first matrix:')
    for _ in range(n1):
        pass

    print('Enter size of second matrix:', end=' ')
    matrix2, n2, m2 = read_matrix_with_size()

    print('Enter second matrix:')
    for _ in range(n2):
        pass

    if n1 != n2 or m1 != m2:
        print('The operation cannot be performed.')
        return

    result = []
    for i in range(n1):
        result.append([matrix1[i][j] + matrix2[i][j] for j in range(m1)])

    print('The result is:')
    print_matrix(result)


def multiply_by_constant():
    print('Enter size of matrix:', end=' ')
    matrix, n, m = read_matrix_with_size()

    print('Enter matrix:')
    for _ in range(n):
        pass

    k = float_if_needed(input('Enter constant: '))

    result = [[matrix[i][j] * k for j in range(m)] for i in range(n)]

    print('The result is:')
    print_matrix(result)


def multiply_matrices():
    print('Enter size of first matrix:', end=' ')
    A, n1, m1 = read_matrix_with_size()

    print('Enter first matrix:')
    for _ in range(n1):
        pass

    print('Enter size of second matrix:', end=' ')
    B, n2, m2 = read_matrix_with_size()

    print('Enter second matrix:')
    for _ in range(n2):
        pass

    if m1 != n2:
        print('The operation cannot be performed.')
        return

    result = [[0 for _ in range(m2)] for _ in range(n1)]

    for i in range(n1):
        for j in range(m2):
            for k in range(m1):
                result[i][j] += A[i][k] * B[k][j]

    print('The result is:')
    print_matrix(result)


def transpose_main(matrix):
    return [list(row) for row in zip(*matrix)]


def transpose_side(matrix):
    return [list(row)[::-1] for row in zip(*matrix[::-1])]


def transpose_vertical(matrix):
    return [row[::-1] for row in matrix]


def transpose_horizontal(matrix):
    return matrix[::-1]


def transpose_matrix():
    print('1. Main diagonal')
    print('2. Side diagonal')
    print('3. Vertical line')
    print('4. Horizontal line')
    choice = input('Your choice: > ')

    print('Enter matrix size:', end=' ')
    matrix, n, m = read_matrix_with_size()

    print('Enter matrix:')
    for _ in range(n):
        pass

    if choice == '1':
        result = transpose_main(matrix)
    elif choice == '2':
        result = transpose_side(matrix)
    elif choice == '3':
        result = transpose_vertical(matrix)
    elif choice == '4':
        result = transpose_horizontal(matrix)
    else:
        return

    print('The result is:')
    print_matrix(result)

def determinant(matrix):
    n = len(matrix)

    # Базовые случаи
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]

    # Разложение по первой строке
    det = 0
    for col in range(n):
        minor = [row[:col] + row[col+1:] for row in matrix[1:]]
        det += ((-1) ** col) * matrix[0][col] * determinant(minor)

    return det


def calculate_determinant():
    print('Enter matrix size:', end=' ')
    matrix, n, m = read_matrix_with_size()

    print('Enter matrix:')
    for _ in range(n):
        pass

    if n != m:
        print('Cannot calculate determinant of a non-square matrix.')
        return

    det = determinant(matrix)

    print('The result is:')
    print(det)

def matrix_of_cofactors(matrix):
    n = len(matrix)
    cof = []

    for i in range(n):
        row = []
        for j in range(n):
            minor = [r[:j] + r[j+1:] for r in (matrix[:i] + matrix[i+1:])]
            row.append(((-1) ** (i + j)) * determinant(minor))
        cof.append(row)

    return cof


def inverse_matrix():
    print('Enter matrix size:', end=' ')
    matrix, n, m = read_matrix_with_size()

    print('Enter matrix:')
    for _ in range(n):
        pass

    if n != m:
        print('This matrix doesn\'t have an inverse.')
        return

    det = determinant(matrix)

    if det == 0:
        print('This matrix doesn\'t have an inverse.')
        return

    cof = matrix_of_cofactors(matrix)
    adj = transpose_main(cof)
    inv = [[adj[i][j] / det for j in range(n)] for i in range(n)]

    print('The result is:')
    print_matrix(inv)


def main():
    while True:
        print('1. Add matrices')
        print('2. Multiply matrix by a constant')
        print('3. Multiply matrices')
        print('4. Transpose matrix')
        print('5. Calculate a determinant')
        print('6. Inverse matrix')
        print('0. Exit')

        choice = input('Your choice: > ')

        if choice == '0':
            break
        elif choice == '1':
            add_matrices()
        elif choice == '2':
            multiply_by_constant()
        elif choice == '3':
            multiply_matrices()
        elif choice == '4':
            transpose_matrix()
        elif choice == '5':
            calculate_determinant()
        elif choice == '6':
            inverse_matrix()



if __name__ == '__main__':
    main()