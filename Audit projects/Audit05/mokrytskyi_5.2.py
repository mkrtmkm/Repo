m = int(input())
N = list(map(int, input().split()))
for i in range(len(N)):
    if N[i] >= 0:
        N[i] += 2
print(*N)
