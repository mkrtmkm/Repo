n = int(input())
array = list(map(int, input().split()))

counts = {}
for num in array:
    counts[num] = counts.get(num, 0) + 1

unique_elements = []
for num in array:
    if counts[num] == 1:
        unique_elements.append(num)

print(*unique_elements)