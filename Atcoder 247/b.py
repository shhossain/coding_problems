h, w = map(int, input().split())
s = [0] * w
for i in range(h):
    ip = input()
    for j in range(w):
        if ip[j] == '#':
            s[j] += 1

for i in s:
    print(i,end=" ")