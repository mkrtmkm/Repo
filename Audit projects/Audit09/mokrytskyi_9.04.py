n = int(input())
array = list(map(int, input().split()))

counts = {}
for num in array:
    counts[num] = counts.get(num, 0) + 1

result = []
seen = set()
for num in reversed(array):
    if counts[num] > 1 and num not in seen:
        result.append(num)
        seen.add(num)

if result:
    print(*reversed(result))
else:
    print("NO")
