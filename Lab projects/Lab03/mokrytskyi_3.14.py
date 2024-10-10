import sys
import math
from math import log10

n = int(input())
sys.set_int_max_str_digits(0)
res = 0

for i in range(2, n + 1):
    res += log10(i)
print(int(res) + 1)