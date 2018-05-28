# XXX slow. but works.
# target = 10
target = 2000000
primes = [2,3]

def is_prime(i):
    for p in primes:
        if i % p == 0:
            return False
    return True

i = max(primes)+2
while i<target:
    if is_prime(i):
        primes.append(i)
        print(i)
    i += 2
print(sum(primes))

