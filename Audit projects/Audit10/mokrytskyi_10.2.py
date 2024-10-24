def input_matrix(n):
    matrix = []
    for i in range(n):
        row = [int(x) for x in input().split()]
        matrix.append(row)
    return matrix

def print_matrix(matrix):
    m = len(matrix)
    n = len(matrix[0])
    for i in range(m):
        for j in range(n):
            print(matrix[i][j], end=" ")
        print()
    print()

def solve(n, m):
    matrix = [[i * m + j + 1 for j in range(m)] for i in range(n)]
    return matrix

n, m = map(int, input().split())
matr = solve(n, m)
print_matrix(matr)


