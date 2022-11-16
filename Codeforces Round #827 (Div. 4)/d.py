from math import gcd
from collections import defaultdict

for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    m = defaultdict(int)

    for i in range(n):
        m[a[i]] = i + 1

    ans = -1
    for i in range(1,1000+1):
        for j in range(1,1000+1):
            if m[i] and m[j] and gcd(i,j)==1:
                ans = max(ans,m[i]+m[j])
    print(ans)