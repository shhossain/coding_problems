import math

T = int(input())
for _ in range(T):
    N = int(input())
    S = input()
    num = int(S, 2)
    a = int(math.log2(num))
    remaining = num - 2**a
    if remaining == 0:
        print("NO")
        continue
    b = int(math.log2(remaining))
    if remaining - 2**b == 0:
        print("NO")
        continue
    c = int(math.log2(remaining - 2**b))
    if c <= b:
        print("NO")
    else:
        print("YES")
