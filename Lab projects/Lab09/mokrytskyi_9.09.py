def find_most_popular(votes):
    count = {}
    for num in votes:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

    max_frequency = max(count.values())
    candidates = {num for num, freq in count.items() if freq == max_frequency}
    return min(candidates)

n = int(input())
results = []

for _ in range(n):
    v = int(input())
    votes = []
    for _ in range(v):
        votes.append(int(input()))
    results.append(find_most_popular(votes))

print("\n".join(map(str, results)))
