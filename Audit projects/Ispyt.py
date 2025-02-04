# Рекурсивний метод обрахунку числа Фібоначі
def Fib1(n):
    if n == 0 or n == 1:
        return 1
    else:
        return Fib1(n - 1) + Fib1(n - 2)

# Нерекурсивний метод обрахунку числа Фібоначі
def Fib2(n):
    F1 = F2 = 1
    for i in range(2, n + 1):
        F2, F1 = F1, F1 + F2
    return F1

# Обчислення НСД
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Реверс числа
def reverse(n):
    reserved = 0
    while n > 0:
        reserved = reserved * 10 + n % 10
        n //= 10
    return reserved

# Сума цифр числа
def summa(n):
    summa = 0
    while n > 0:
        last_number = n % 10
        summa += last_number
        n //= 10
    return summa

# Переведення чисел між різними системами числення
def convert_base_custom(num_str, from_base, to_base):
    decimal_num = 0
    for digit in num_str:
        decimal_num = decimal_num * from_base + int(digit)
        
    if decimal_num == 0:
        return "0"

    result = ""
    while decimal_num > 0:
        remainder = decimal_num % to_base
        result = str(remainder) + result
        decimal_num //= to_base

    return result