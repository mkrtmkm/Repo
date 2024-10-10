n = int(input())
array = [int(x) for x in input().split()]

for j in range(n-1):
    for i in range(n-1 - j):
        if array[i] > array[i+1]:
            array[i], array[i+1] = array[i+1], array[i]

    print(*array)


