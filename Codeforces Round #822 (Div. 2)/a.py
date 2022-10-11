from itertools import permutations


def cost(a):
    # a will always be a list of 3 elements
    if len(a) < 3:
        return -1

    sorted_a = sorted(a)
    middle = sorted_a[1]
    c = 0
    for i in a:
        if i != middle:
            c += abs(i - middle)
    return c


def minimum_cost(l):
    # get permutations of l that are of length 3
    perms = permutations(l, 3)
    cst = None
    for p in perms:
        c = cost(p)
        if c != -1:
            if cst is None:
                cst = c
            else:
                cst = min(cst, c)
    return cst if cst is not None else 0


t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    print(minimum_cost(l))
