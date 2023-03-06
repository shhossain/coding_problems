from math import factorial as f
from random import randint


def isPrime(n, k=5):
    if n < 2:
        return False
    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]:
        if n % p == 0:
            return n == p
    s, d = 0, n-1
    while d % 2 == 0:
        s, d = s+1, d/2
    for i in range(k):
        x = pow(randint(2, n-1), d, n)
        if x == 1 or x == n-1:
            continue
        for r in range(1, s):
            x = (x * x) % n
            if x == 1:
                return False
            if x == n-1:
                break
        else:
            return False
    return True


def ncr(n, r):
    return f(n) // f(r) // f(n-r)


def solve():
    for x in range(int(input())):
        n = int(input())
        a = list(map(int, input().split()))
        count = 0
        for i in a:
            if isPrime(i):
                count += 1
        if count >= 3:
            v = ncr(count, 3)
        else:
            v = 0
        print("Case {}: {}".format(x+1, v))


solve()
