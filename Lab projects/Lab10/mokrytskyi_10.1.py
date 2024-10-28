def input_matrix(n):
    matrix = []
    for i in range(n):
        row = [int(x) for x in input().split()]
        matrix.append(row)
    return matrix

def print_matrix(matrix):
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        for j in range(m):
            print(matrix[i][j], end=" ")
        print()
    print()

def solve(matrix, n):
    count = 0
    ssum = 0
    for i in range(n):
        for j in range(n):
            if matrix[i][j] % 2 == 0 and matrix[i][j] < 0:
                count += 1
                ssum += matrix[i][j]
    return count, ssum

n = int(input())
matr = input_matrix(n)
c, s = solve(matr, n)
print(c, s)
