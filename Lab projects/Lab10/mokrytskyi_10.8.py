def input_matrix(n):
    matrix = []
    for i in range(n):
        row = [int(x) for x in input().split()]
        matrix.append(row)
    return matrix

n = int(input())
matrix = input_matrix(n)
suma_main = 0
suma_side = 0

for i in range(n):
    suma_main += matrix[i][i]
    suma_side += matrix[i][n-i-1]

print(suma_main, suma_side)