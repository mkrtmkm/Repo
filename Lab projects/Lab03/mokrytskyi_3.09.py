n = int(input())
count = 0
num = 1

while count < n:
    if num % 2 != 0 and num % 3 != 0 and num % 5 != 0:
        print(num, end=" ")
        count += 1
    num += 1