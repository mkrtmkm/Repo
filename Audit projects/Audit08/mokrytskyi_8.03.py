def pas(n, k):
    if k == 0 or k == n:
        return 1
    return pas(n-1, k-1) + pas(n-1, k)

def tria(n):
    for i in range(n):
        for j in range(i + 1):
            print(pas(i, j), end=' ')
        print()


n = int(input())
tria(n)



'''from math import*
def C1(n, k):
    return factorial(n) // factorial(k) // factorial(n-k)

def print_pascal(n):
    for i in range(n):
        for j in range(i+1):
            print(C1(i, j), end = ' ')
        print()
print_pascal(10)'''