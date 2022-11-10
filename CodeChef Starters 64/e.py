from functools import reduce
from math import gcd


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    gv = reduce(lambda x, y: gcd(x, y), a)

    c = 0
    for i in a:
        if i//gv > 1:
            c += 1

    print(c)
