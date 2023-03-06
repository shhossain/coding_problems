def dist(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)


for _ in range(int(input())):
    n, x1, y1, x2, y2 = map(int, input().split())
    d1 = dist(x1, y1, x2, y2)

    v1xy = (0, y1)
    v2xy = (n+1, y1)
    v3xy = (x1, 0)
    v4xy = (x1, n+1)

    td1 = dist(x1, y1, *v1xy)
    td2 = dist(x1, y1, *v2xy)
    td3 = dist(x1, y1, *v3xy)
    td4 = dist(x1, y1, *v4xy)

    min_d1 = min(td1, td2, td3, td4)

    v1xy = (0, y2)
    v2xy = (n+1, y2)
    v3xy = (x2, 0)
    v4xy = (x2, n+1)

    td1 = dist(x2, y2, *v1xy)
    td2 = dist(x2, y2, *v2xy)
    td3 = dist(x2, y2, *v3xy)
    td4 = dist(x2, y2, *v4xy)

    min_d2 = min(td1, td2, td3, td4)

    d2 = min_d1 + min_d2
    print(min(d1, d2))
