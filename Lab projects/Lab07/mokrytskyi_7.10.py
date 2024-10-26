def to_decimal(number, base):
    decimal_value = 0
    power = 1

    for digit in reversed(number):
        if '0' <= digit <= '9':
            value = ord(digit) - ord('0')
        else:
            value = ord(digit) - ord('A') + 10

        decimal_value += value * power
        power *= base

    return decimal_value

def from_decimal(number, base):
    if number == 0:
        return '0'

    symbols = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = []

    while number > 0:
        res.append(symbols[number % base])
        number //= base

    return ''.join(res[::-1])

m, k = map(int, input().split())
n = input().strip()

decimal_value = to_decimal(n, m)
result_k = from_decimal(decimal_value, k)

print(result_k)
