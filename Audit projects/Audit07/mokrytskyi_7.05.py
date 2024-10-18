def convert_to_dec(n, k=10):
    pow_k = 1
    converted = 0
    while n > 0:
        last = n % 10
        converted += last * pow_k
        pow_k *= k
        n = n // 10
    return converted

def convert_from_dec(c, k=10):
    pow_10 = 1
    converted = 0
    while c > 0:
        last = c % k
        converted += last * pow_10
        pow_10 *= 10
        c = c // k
    return converted

A = int(input())
B = int(input())

decA = convert_to_dec(A, 2)
decB = convert_to_dec(B, 2)

c = decA + decB

decC = convert_from_dec(c, 2)
print(decC)

