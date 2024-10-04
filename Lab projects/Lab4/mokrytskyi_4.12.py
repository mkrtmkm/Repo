suma = 0
while True:
    n = int(input())
    if n != 0:
        if n % 2 == 0:
            suma += n
    else:
        break
print(suma)