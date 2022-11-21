n,k = map(int, input().split())
a = list(map(int, input().split()))

a = a[k:]

k = min(n,k)
a = a + [0] * k
print(*a)