def collatz(n):
    if n%2==0:
        return n/2
    else:
        return 3*n + 1

def count_collatz(n):
    i = 1
    while n!=1:
        n = collatz(n)
        i+=1
    return i

m = 0
result = 0
for n in range(1, 1000000):
    c = count_collatz(n)
    print("n=%d c=%d" % (n, c))
    if m<c:
        m = c
        result = n
print(result)


