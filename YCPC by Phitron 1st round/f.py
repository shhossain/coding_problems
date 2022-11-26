
# n = 5
# 12345
# 2   4
# 3   3
# 4   2


n = int(input())


a = [i for i in range(1, n+1)]

s, e = 0, n-1
for i in range(n-1):
    if i == 0:
        for i in a:
            print(i, end="")
        print()
        s += 1
        e -= 1

    else:
        print(a[s],end="")
        print(" "*(n-2),end="")
        print(a[e])
        s += 1
        e -= 1

for i in a[::-1]:
    print(i,end="")
print()
