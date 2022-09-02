def gcd(a,b):
    gcd = 1
    for k in range(1, min(a,b) + 1):
        if a % k == 0 and b % k == 0:
            gcd = k
    return gcd


print(gcd(12, 16))