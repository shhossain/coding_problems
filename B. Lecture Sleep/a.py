from collections import defaultdict


n,k = map(int, input().split())
m = defaultdict(list)

a = list(map(int, input().split()))
s = list(map(int, input().split()))

for i in range(n):
    m[a[i]].append(s[i])

print(dict(m))


