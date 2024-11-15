a = input().strip()
b = input().strip()

counts_a = {}
counts_b = {}

for char in a:
    counts_a[char] = counts_a.get(char, 0) + 1

for char in b:
    counts_b[char] = counts_b.get(char, 0) + 1

for char in counts_b:
    if counts_b[char] > counts_a.get(char, 0):
        print("No")
        break
else:
    print("Ok")