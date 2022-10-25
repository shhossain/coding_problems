t = int(input())
for i in range(t):
    n = int(input())
    a1 = list(map(int, input().split()))
    a2 = list(map(int, input().split()))
    a = [[i, j] for i, j in zip(a1, a2)]
    b = sorted(a, key=lambda x: x[1])
    t = 0
    for i in range(len(b)):
        if i < len(b)-1:
            b[i+1][0] += b[i][1]
        t += b[i][0]
    print(t)
