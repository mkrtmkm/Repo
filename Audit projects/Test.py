def convert_base_custom(num, from_base, to_base):
    decimal_num = 0
    num = str(num)
    for digit in num:
        decimal_num = decimal_num * from_base + int(digit)

    if decimal_num == 0:
        return 0

    result = ""
    while decimal_num > 0:
        remainder = decimal_num % to_base
        result = str(remainder) + result
        decimal_num //= to_base

    return result

print(convert_base_custom(10, 10, 6))