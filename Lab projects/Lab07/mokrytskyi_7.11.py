def from_decimal(number, base):
    if number == 0:
        return '0'

    symbols = "0123456789abcdefghijklmnopqrstuvwxyz"
    res = []

    while number > 0:
        res.append(symbols[number % base])
        number //= base

    return ''.join(res[::-1])

def is_palindrom(s):
    return s == s[::-1]


n = int(input().strip())
res = []


for base in range(2, 37):
    rep = from_decimal(n, base)
    if is_palindrom(rep):
        res.append(base)


if len(res) == 0:
    print("none")
elif len(res) == 1:
    print("unique")
    print(res[0])
else:
    print("multiple")
    print(" ".join(map(str, res)))
