a, b, x, y, z = map(float, input().split())
if ((a > x and b > y) or
        (a > x and b > z) or
        (a > y and b > x) or
        (a > y and b > z) or
        (a > z and b > x) or
        (a > z and b > y)):
    print("1")
else:
    print("0")