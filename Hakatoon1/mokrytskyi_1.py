N, P, Q, K = [int (d) for (d) in input().split()]
# N = 30, P = 2, Q = 5, K = 27
n = N//P #к-сть квартир у кожному під'їзді
p = n//Q #к-сть квартир на кожному поверсі під'їзду

q = K//P