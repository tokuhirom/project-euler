import math

r = 600851475143

i=3
while True:
    if r % i == 0:
        print(i)
        r /= i
        if r == 1:
            break

    i+=2


