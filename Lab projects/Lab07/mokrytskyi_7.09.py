def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def reverse(n):
    return int(str(n)[::-1])

def happy_prime(K):
    happy_primes = []
    num = 2

    while len(happy_primes) < K:
        if is_prime(num):
            reversed_num = reverse(num)
            if num != reversed_num and is_prime(reversed_num):
                happy_primes.append(num)
        num += 1

    return happy_primes[-1] if happy_primes[-1] <= 10**6 else -1


K = int(input())
print(happy_prime(K))