n = 100
r = 1
for i in range(1, n):
    r *= i
print(sum(int(n) for n in list(str(r))))
