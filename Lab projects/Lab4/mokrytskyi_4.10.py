n = int(input())
suma = 0
for i in range(100, 1000):
    c = i % 10
    b = i // 10 % 10
    a = i // 100
    if n == 1:
        if a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
            suma += i
    elif n == 2:
        if a < b < c:
            suma += 1
    elif n == 3:
        if a % 2 != 0 and b % 2 != 0 and c % 2 != 0:
            suma += i
    elif n == 4:
        if a > b > c:
            suma += 1
    elif n == 5:
        if i == a ** 3 + b ** 3 + c ** 3:
            suma += i
    else:
        if a != b or a != c or b != c:
            suma += 1
print(suma)