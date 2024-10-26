def is_palindrom(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrom(s[1:-1])

def invert(s):
    if len(s) == 0:
        return ''
    return s[-1] + invert(s[:-1])

def replace(s, old, new):
    if len(s) == 0:
        return ''
    if s[0] == old:
        return new + replace(s[1:], old, new)
    else:
        return s[0] + replace(s[1:], old, new)

s = input()
old = input()
new = input()
print(is_palindrom(s))
print(invert(s))
print(replace(s, old, new))