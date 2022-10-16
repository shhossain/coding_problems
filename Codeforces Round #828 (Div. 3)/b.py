t = int(input())
for _ in range(t):
    n, q_no = map(int, input().split())
    a = list(map(int, input().split()))
    sum_a = sum(a)
    e = 0  # evens
    for i in range(len(a)):
        if a[i] % 2 == 0:
            e += 1
    o = len(a) - e  # odds
    for _ in range(q_no):
        d, v = map(int, input().split())
        if d == 0:
            t_sum = sum_a + (v * e)
            sum_a = t_sum
            if v % 2 != 0:
                temp = e
                e -= temp
                o += temp
        else:
            t_sum = sum_a + (v * o)
            sum_a = t_sum
            if v % 2 != 0:
                temp = o
                o -= temp
                e += temp
        print(sum_a)

