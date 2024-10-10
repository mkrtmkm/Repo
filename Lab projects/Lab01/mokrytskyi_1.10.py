from math import*
S, R1 = [float(d) for d in input().split()]
S1 = pi*R1**2
S2 = S1 - S
R2 = sqrt(S2/pi)
print(f"{R2:.2f}")