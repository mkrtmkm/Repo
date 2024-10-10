from math import*
lst1 = list(map(float, input().split()))
lst2 = list(map(float, input().split()))

v1 = (lst1[2] - lst1[0], lst1[3] - lst1[1])
v2 = (lst2[2] - lst2[0], lst2[3] - lst2[1])

length_v1 = sqrt(v1[0]**2 + v1[1]**2)
length_v2 = sqrt(v2[0]**2 + v2[1]**2)

v_sum = (v1[0] + v2[0], v1[1] + v2[1])

scal_prod = v1[0] * v2[0] + v1[1] * v2[1]

vec_prod = v1[0] * v2[1] - v1[1] * v2[0]

area = abs(vec_prod) / 2.0

print(f"{length_v1:.9f} {length_v2:.9f}")
print(f"{v_sum[0]:.9f} {v_sum[1]:.9f}")
print(f"{scal_prod:.9f} {vec_prod:.9f}")
print(f"{area:.9f}")
