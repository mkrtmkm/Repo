n = input()
missing_digits = []
n1 = ""
count = 0
all_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

for i in n:
    if i != '+':
      n1 += i

for i in all_digits:
    if i not in n1:
        missing_digits += i
print(len(missing_digits))
print(*missing_digits)