for _ in range(int(input())):
    l, r, x = map(int, input().split())
    a, b = map(int, input().split())

    al, ra, bl, rb,ab = abs(a-l), abs(r-a), abs(b-l), abs(r-b), abs(a-b)
    ans = -1
    if a == b:
        ans = 0
    elif ab >= x:
        ans = 1
    elif (al < x and ra < x) or (bl < x and rb < x):
        ans = -1
    else:
        if al < x:
            if rb >= x:
                ans = 2
            else:
                ans = 3
        elif ra < x:
            if bl >= x:
                ans = 2
            else:
                ans = 3
        else:
            ans = 2
    
    print(ans)
