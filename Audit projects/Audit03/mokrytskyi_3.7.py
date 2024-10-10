n = int(input())
b = n
i = 0

while n > 0:
    d = n % 10
    i = i * 10 + d
    n //= 10

if i == b:
    print("Yes")
else:
    print("No")
