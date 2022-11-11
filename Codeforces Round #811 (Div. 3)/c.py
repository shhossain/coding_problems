def solve(n):
    a = [i for i in range(10)]
    s = n
    arr = []
    while True:
        v = 0
        if s > 9:
            v = a.pop()
        else:
            l = len(a) - 1
            if s > l:
                v = a.pop()
            else:
                v = a.pop(s)
        arr.append(v)
        d = s - v
        if d == 0:
            arr.sort()
            return arr
        else:
            s = d


for _ in range(int(input())):
    n = int(input())
    print("".join(map(str, solve(n))))
