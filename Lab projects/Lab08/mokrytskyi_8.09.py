def convert_to_base13(n):
    if n == 0:
        return ""

    remainder = n % 13

    if remainder == 10:
        remainder_char = "A"
    elif remainder == 11:
        remainder_char = "B"
    elif remainder == 12:
        remainder_char = "C"
    else:
        remainder_char = str(remainder)
    return convert_to_base13(n // 13) + remainder_char


def to_base13(n):
    if n == 0:
        return "0"
    return convert_to_base13(n)

n = int(input())
print(to_base13(n))
