def unique(n):
    str_n = str(n)
    return len(set(str_n)) == len(str_n)

a, b = map(int, input().split())
unique_numbers = [str(i) for i in range(a, b + 1) if unique(i)]
print(" ".join(unique_numbers))