import math

def triangle(a, b, c):
    assert a + b > c and a + c > b and b + c > a, "Умова трикутника не виконується"

    p = (a + b + c) / 2

    S = math.sqrt(p*(p - a)*(p - b)*(p - c))
    return S
a, b, c = map(float, input().split())

try:
    print(f"Площа трикутника: {triangle(a, b, c):.2f}")
except AssertionError as e:
    print(e)