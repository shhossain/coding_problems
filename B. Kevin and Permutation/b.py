for _ in range(int(input())):
    n = int(input())
    a = range(1, n+1)
    r = [a[i//2] if i % 2 == 1 else a[((i)//2)+n//2] for i in range(0, n)]
    print(*r)
