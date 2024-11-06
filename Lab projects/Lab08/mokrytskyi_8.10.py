def generate(permutation, n):
    if len(permutation) == n:
        print(" ".join(map(str, permutation)))
        return

    for i in range(1, n + 1):
        if i in permutation:
            continue
        permutation.append(i)
        generate(permutation, n)
        permutation.pop()

def lexicographic(n):
    generate([], n)


n = int(input())
lexicographic(n)

