target = 10001
# target = 6
primes = []

def is_prime(i):
    for p in primes:
        if i % p == 0:
            return False
    return True

i = 2
while len(primes) < target:
    if is_prime(i):
        primes.append(i)
    i += 1
print(primes[-1])

