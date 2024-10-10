n = int(input())
lst = list(map(float, input().split()))
suma = 0
count = 0

for i in lst:
    if i > 0:
        suma += i
        count += 1

if count > 0:
    frac = suma / count
    print(f"{frac:.2f}")
else:
    print("Not Found")
