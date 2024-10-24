def multiply_matrices(A, B, n_a, m_a, n_b, m_b):
    if m_a != n_b:
        return -1

    C = [[0] * m_b for _ in range(n_a)]

    for i in range(n_a):
        for j in range(m_b):
            for k in range(m_a):
                C[i][j] += A[i][k] * B[k][j]
    return C

n_a, m_a = map(int, input().split())
A  = [list(map(int, input().split())) for _ in range(n_a)]

n_b, m_b = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(n_b)]

res = multiply_matrices(A, B, n_a, m_a, n_b, m_b)

if res == -1:
    print(-1)
else:
    print(n_a, m_b)
    for row in res:
        print(" ".join(map(str, row)))
