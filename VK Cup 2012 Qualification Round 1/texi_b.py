n = int(input())
arr = list(map(int, input().split()))

total = 0
c3 = 0
c2 = 0
c1 = 0

for i in arr:
    if i == 4:
        total += 1
    elif i == 3:
        c3 += 1
    elif i == 2:
        c2 += 1
    elif i == 1:
        c1 += 1


while c3 > 0 and c1 > 0:
    c3 -= 1
    c1 -= 1
    total += 1

if c3 > 0:
    total += c3

v = c2 // 2
total += v
c2 -= v * 2

while c2 > 0 and c1 > 1:
    c2 -= 1
    c1 -= 2
    total += 1

while c2 > 0 and c1 > 0:
    c2 -= 1
    c1 -= 1
    total += 1

if c2 > 0:
    total += c2

if c1 > 0:
    v = c1 // 4
    total += v
    c1 -= v * 4

    if c1 > 0:
        total += 1


print(total)
