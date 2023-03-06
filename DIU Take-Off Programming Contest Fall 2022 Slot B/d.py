a,b = map(int,input().split())

ans = a-b
if a > 12 and b&1:
    ans = a + b
elif a <= 12 and b%2 == 0:
    ans = a + b

print(ans)
