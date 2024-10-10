n = int(input())
lst = list(map(float, input().split()))
suma = 0
k = 0
for i in range(2, n, 3):
    if lst[i] > 0:
        k += 1
        suma += lst[i]
print(f"{k}, {suma:.2f}")