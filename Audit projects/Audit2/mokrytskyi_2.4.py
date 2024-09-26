x = int(input())
if -1000 <= x < 13:
    y = 3*x**3 - 2*x**2 - 3*x - 4
    print(f"При x = {x} y = {y}")
elif 13<=x<1000:
    y = 3*x**3 + 4*x**2 + 5*x + 6
    print(f"При x = {x} y = {y}")