from math import gcd

n = int(input())
a = list(map(int, input().split()))
ga = gcd(*a)


def is_integer(n):
    return n == int(n)


c = 0
for i in a:
    v = i / ga
    if v == 1:
        continue
    v2 = v/2
    v3 = v/3
    if is_integer(v2) and is_integer(v3):
        if v2 < v3:
            c += v2
        else:
            c += v3
    elif is_integer(v2):
        c += v2
    elif is_integer(v3):
        c += v3

    if not (i % 2 == 0 or i % 3 == 0):
        c = -1
        break

print(int(c))
