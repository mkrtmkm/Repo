a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())

A = [[a1, b1], [a2, b2]]
detA = A[0][0] * A[1][1] - A[0][1] * A[1][0]

A1 = [[c1, b1], [c2, b2]]
detA1 = A1[0][0] * A1[1][1] - A1[0][1] * A1[1][0]

A2 = [[a1, c1], [a2, c2]]
detA2 = A2[0][0] * A2[1][1] - A2[0][1] * A2[1][0]

x1 = detA1 / detA
x2 = detA2 / detA
print(f"{x1:.3f}")
print(f"{x2:.3f}")
