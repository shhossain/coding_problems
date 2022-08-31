runs = int(input())
for i in range(runs):
    n = int(input())
    a = list(map(int, input().split()))
    val = 0
    if len(a) == 1:
        val = a[0] * a[0]
    else:
        val = 1
        for num in a:
            val *= num

    print("Case {}: {}".format(i + 1, val))
