from math import*

def is_full_square(n):
    sqr = sqrt(n)
    if sqr == int(sqr):
        return True
    else:
        return False

def is_power_of_five(n):
    while n > 1:
        if n % 5:
            return False
        n //= 5
    return True

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

lst = [int(x) for x in input().split()]
for x in lst:
    if is_full_square(x):
        print(x, "- є повним квадратом")
    if is_power_of_five(x):
        print(x, "- є степенем п'ятірки")
    if is_prime(x):
        print(x, "- є простим числом")