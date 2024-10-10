import sys
sys.set_int_max_str_digits(0)

n = int(input())
res = 1
i = 0

if n == 1:
    print(1)
else:
    while res < n:
        i += 1
        res *= i
    print(i)