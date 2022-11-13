# ・For every string, the first character is one of H, D, C, and S.
# ・For every string, the second character is one of A, 2, 3, 4, 5, 6, 7, 8, 9, T, J, Q, K.


a = []
n = int(input())
for _ in range(n):
    a.append(input())


i = 0
flag3 = True
while i <= n:
    for j in range(i+1, n):
        if a[i] == a[j]:
            flag3 = False
            break
    i+=1



flag1 = False
flag2 = False
m1 = ["H", "D", "C", "S"]
m2 = ["A", "2", "3", "4", "5","6","7", "8", "9", "T", "J", "Q", "K"]
for i in range(n):
    if a[i][0] in m1:
        flag1 = True

    if a[i][1] in m2:
        flag2 = True


if flag1 and flag2 and flag3:
    print("Yes")
else:
    print("No")
