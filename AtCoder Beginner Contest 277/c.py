# 4
# 1 4
# 4 3
# 4 10
# 8 3

from collections import defaultdict


store = defaultdict(int)
for _ in range(int(input())):
    a, b = map(int, input().split())
    v = store[a]
    if v < b:
        store[a] = b

ans = 1
keys = sorted(list(store.keys()))
i = 0
while i < len(store):
    if keys[i] <= ans:
        v = store[keys[i]]
        ans = max(ans,v)
    else:
        break
    i+=1

print(ans)

    
