n = int(input())
input_numbers = list(map(int, input().split()))

seen = [False] * (2 * 10**6 + 1)
count = 0

for num in input_numbers:
    abs_num = abs(num)
    if not seen[abs_num]:
        seen[abs_num] = True
        count += 1

print(count)
