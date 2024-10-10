def func(n):
    flag = 1
    if n == 1:
        flag = False
    else:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                flag = False
                break
    return flag

n = int(input())
for i in range(n, 2*n):
    if func(i) == 1 and func(i+2) == 1 <= 2*n:
        print(i,i+2)