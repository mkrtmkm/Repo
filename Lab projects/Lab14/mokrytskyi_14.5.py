from math import sqrt

a, b, c = map(int, input().split())
D = b**2 - 4*a*c

try:
    assert a != 0
except AssertionError:
    print("Рівняння не є квадратним")
else:
    try:
        assert D >= 0
    except AssertionError:
        print("Рівняння не має коренів на множині дійсних чисел")
    else:
        if D == 0:
            x = -b / (2*a)
            print("Рівняння має один корінь:")
            print(f"{x = }")
        else:
            x1 = (-b + sqrt(D)) / (2*a)
            x2 = (-b - sqrt(D)) / (2*a)
            print("Рівняння має два корені:")
            print(f"{x1 = }" "\n"
                  f"{x2 = }")

