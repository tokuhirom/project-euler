results = []

for i in range(100,1001):
    for j in range(100,1001):
        m = i*j
        if str(m)[::-1] == str(m):
            results.append(m)

r = sorted(results)
print(r[-1])

