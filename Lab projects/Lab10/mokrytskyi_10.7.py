def input_matrix(n):
    matrix = []
    for i in range(n):
        row = [int(x) for x in input().split()]
        matrix.append(row)
    return matrix

def new_matrix(matrix, r, c):
    new = []
    for i in range(r):
        new.append(matrix[i][:c])
    return new

n = int(input())
matrix = input_matrix(n)
r, c = map(int, input().split())

new = new_matrix(matrix, r, c)

for i in range(r):
    print(" ".join(map(str, new[i])))
