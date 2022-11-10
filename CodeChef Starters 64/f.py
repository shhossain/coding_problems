import math


def primeFactors(n):

    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n / 2

    for i in range(3, int(math.sqrt(n))+1, 2):
        while n % i == 0:
            factors.append(i)
            n = n / i
    if n > 2:
        factors.append(n)

    f = set(factors)
    f = map(int, f)
    return f


for _ in range(int(input())):
    a, b = map(int, input().split())
    fb = primeFactors(b)
    flag = True
    for f in fb:
        if a % f != 0:
            flag = False
            break

    if flag:
        print("YES")
    else:
        print("NO")
