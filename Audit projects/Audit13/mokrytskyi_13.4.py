def input_matrix(filename):
    matrix = []
    with open(filename, "r") as file:
        for line in file:
            row = list(map(int, line.split()))
            matrix.append(row)
    return matrix

def write_matrix(matrix, filename):
    with open(filename, 'w') as file:
        for row in matrix:
            file.write(" ".join(map(str, row)) + '\n')

def add_matrices(matrix1, matrix2):
    n = len(matrix1)
    m = len(matrix2)
    if n != m:
        raise ValueError("Матриці мають різні розміри")

    result = []
    for i in range(n):
        row = [matrix1[i][j] + matrix2[i][j] for j in range(n)]
        result.append(row)
    return result

def multiply_matrices(matrix1, matrix2):
    n = len(matrix1)
    if len(matrix2) != n:
        raise ValueError("Такі матриці не множаться")

    result = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(sum(matrix1[i][k] * matrix2[k][j] for k in range(n)))
        result.append(row)
    return result

matrix1 = input_matrix('input13.4.1.txt')
matrix2 = input_matrix('input13.4.2.txt')

sum_matrix = add_matrices(matrix1, matrix2)
product_matrix = multiply_matrices(matrix1, matrix2)

write_matrix(sum_matrix, 'sum_matrix.txt')
write_matrix(product_matrix, 'product_matrix.txt')
