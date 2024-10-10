s = input()

count = 0
word = False

for c in s:
    if c.isalnum():
        if not word:
            word = True
            count += 1
    else:
        word = False

print(count)