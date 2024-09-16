n = int(input())
condition1 = n % 2 == 0
condition2 = n < 0 and n % 3 == 0
if condition1 != condition2:
    print("YES")
else:
    print("NO")