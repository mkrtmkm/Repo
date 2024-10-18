n = int(input())

total = 9 * (10 ** (n - 1))
without_seven = 8 * (9 ** (n - 1))
with_seven = total - without_seven

print(with_seven)
