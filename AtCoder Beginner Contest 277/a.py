
n,x = map(int, input().split())
a = list(map(int, input().split()))
idx = n
for b,i in enumerate(a):
	if i == x:
		idx = b+1
		break
print(idx) 