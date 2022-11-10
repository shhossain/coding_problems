for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    if a[0] == a[n-1]:
        print("Yes")
    else:
        c = 0
        for i in range(n):
            if a[i]==a[0] and a[n-1]==a[i+1]:
                c = 1
        if c==1:
            print("Yes")
        else:
            print("No")

        