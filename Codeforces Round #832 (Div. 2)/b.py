for _ in range(int(input())):
    n = int(input())
    v = 2
    x = 3*n
    if n%2:
        v = int(n/2) + 1
    else:
        v = int(n/2)

    x = 3*n
    y = 1
    print(v)
    for i in range(v):
        print(y,x)
        y+=3
        x-=3