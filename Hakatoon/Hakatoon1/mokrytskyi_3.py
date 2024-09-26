from math import*
x, y, x1, y1, x2, y2, x3, y3 = [float (d) for (d) in input().split()]
AB = sqrt((x2-x1)**2 + (y2-y1)**2)
BC = sqrt((x3-x2)**2 + (y3-y2)**2)
AC = sqrt((x3-x1)**2 + (y3-y1)**2)
a = ((x2 - x1)*(y-y1) - (y2-y1)*(x-x1))
b = ((x3 - x2)*(y-y2) - (y3-y2)*(x-x2))
c = ((x3 - x1)*(y - y3) - (y3 - y1)*(x - x3))

if a == 0 or b == 0 or c == 0:
    print(1)
else:
    AO = sqrt((x-x1)**2 + (y-y1)**2)
    BO = sqrt((x-x2)**2 + (y-y2)**2)
    CO = sqrt((x-x3)**2 + (y-y3)**2)
    p = (AB + BC + AC)//2
    p1 = (AO + BO + AB)//2
    p2 = (BO + CO + BC)//2
    p3 = (AO + CO + AC)//2
    S1 = sqrt(p1*(p1 - AO)*(p1 - BO)*(p1-AB))
    S2 = sqrt(p2*(p2-BO)*(p2-CO)*(p2-BC))
    S3 = (p3*(p3-AO)*(p3-CO)*(p3-AC))**0.5
    S = sqrt(p*(p-AB)*(p-BC)*(p-AC))
    if S == S1 + S2 + S3:
        print(1)
    else:
        print(0)