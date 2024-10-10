n = int(input())
i = 0
if n % 2 == 1:
    i += 1

while n != 0:
    n = int(input())
    if n % 2 == 1:
        i += 1

print(i)