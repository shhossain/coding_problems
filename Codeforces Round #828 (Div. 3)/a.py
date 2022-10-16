t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    s = input()
    m = {}
    for i in range(len(a)):
        if a[i] in m:
            m[a[i]].add(s[i])
        else:
            m[a[i]] = {s[i]}
    flag = True
    for v in m.values():
        if len(v) > 1:
            flag = False
            break
    if flag:
        print('YES')
    else:
        print('NO')
