# 5
# 4
# 3 1 4 3
# 5
# 1 1 1 1 1
# 1
# 1
# 6
# 6 5 4 3 2 1
# 7
# 1 2 1 7 1 2 1

from collections import defaultdict

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    m = defaultdict(int)
    for i in a:
        m[i] += 1

    a_len = len(a)
    unq_len = len(m)

    for i in a:
        if m[i] > 1:
            m[i] -= 1
            a_len -= 1
        else:
            if a_len != unq_len:
                m[i] -= 1
                a_len -= 1
                unq_len -= 1
        
        if a_len == unq_len:
            break
    
    print(n-a_len)