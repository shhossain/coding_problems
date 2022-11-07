for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    g1 = 0
    g2 = 0

    for i in range(n):
        if i >= 0:
            g1 += a[i]
        else:
            g2 += a[i]

    print(abs(g1)-abs(g2))
