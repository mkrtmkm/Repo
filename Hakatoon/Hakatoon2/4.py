# Вартість упаковок
cost_100 = 100
cost_20 = 30
cost_1 = 2

min_costs = [0] * 1001

for n in range(1, 1001):
    min_cost = n * cost_1

    if n >= 20:
        min_cost = min(min_cost, min_costs[n - 20] + cost_20)

    if n >= 100:
        min_cost = min(min_cost, min_costs[n - 100] + cost_100)

    min_costs[n] = min_cost

n = int(input())
print(min_costs[n])
