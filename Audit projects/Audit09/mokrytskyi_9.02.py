n = int(input())
array = map(int, input().split())

counts = {}
for num in array:
    counts[num] = counts.get(num, 0) + 1

majority_count = n // 2
majority_element = -1
for num, count in counts.items():
    if count > majority_count:
        majority_element = num
        break

print(majority_element)
