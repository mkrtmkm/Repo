n = int(input())
lst = list(map(int, input().split()))

if n > 0:
    lst = [lst[-1]] + lst[:-1]
print(*lst)