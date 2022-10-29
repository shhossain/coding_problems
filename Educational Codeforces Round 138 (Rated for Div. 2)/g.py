T = int(input())

for t in range(T):
    n = int(input())

    while n & 1 == 0:
        n = n >> 1

    print("Case " + str(t + 1) + ": " + str(n))