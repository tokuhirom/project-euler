import sys

l = 20

def prime_factorization(n):
    r = []
    while n > 1:
        for i in range(2, n+1):
            if n%i==0:
                r.append(i)
                n = int(n/i)
                break
    return r

r = []
for j in range(1, l+1):
    p = prime_factorization(j)
    m = r[:]
    for i in p:
        if i not in m:
            r.append(i)
        else:
            for k in range(len(m)):
                if i == m[k]:
                    m.pop(k)
                    break

result = 1
for i in r:
    result *= i
print(result)

