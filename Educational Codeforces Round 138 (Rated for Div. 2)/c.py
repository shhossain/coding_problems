t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if n > 1:
        if a.count(a[0]) == n:
            print(0)
        else:
            print(max(a))
    else:
        print(a[0])
