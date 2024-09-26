n = int(input())
t = 0

if n == 0:
    t = 1
while n > 0:
    n = n // 10
    t += 1
print(t)