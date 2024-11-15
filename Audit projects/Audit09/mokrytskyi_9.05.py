string = input().strip()
counts = {}

for char in string:
    counts[char] = counts.get(char, 0) + 1
max_letter = max(counts.keys())
print(max_letter, counts[max_letter])