def convert_from_dec(c, k=2):
    converted = ""
    while c > 0:
        last = c % k
        converted = str(last) + converted
        c = c // k
    return converted

def create_rule(n):
    if len(n) == 0:
        return ""

    first = n[0]
    if first == "1":
        return "SX" + create_rule(n[1:])
    else:
        return "S" + create_rule(n[1:])

c = int(input())
n = convert_from_dec(c, 2)
print(create_rule(n)[2:])
