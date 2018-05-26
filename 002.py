s = 2
p1 = 1
p2 = 2

while True:
    p1, p2 = p2, p1+p2
    m = p2
    if m>=4000000:
        break
    if m%2 == 0:
        s += m

print(s)
