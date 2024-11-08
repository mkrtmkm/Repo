t = int(input())

for _ in range(t):
    v = int(input())
    votes = [0] * 1001 

    for _ in range(v):
        num = int(input())
        votes[num] += 1  # Збільшуємо кількість голосів для цього числа

    # Знаходимо максимальну кількість голосів
    max_votes = max(votes)

    # Шукаємо найменше число, яке отримало максимальну кількість голосів
    for num in range(1, 1001):
        if votes[num] == max_votes:
            print(num)
            break
