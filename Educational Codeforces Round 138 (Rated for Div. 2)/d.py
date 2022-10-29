t = int(input())
for _ in range(t):
	n,q = map(int,input().split())
	a = list(map(int,input().split()))
	a_sum = sum(a)
	for _ in range(q):
		a,b = map(int,input().split())
		v = abs(a-b)+1
		if v % 2 != 0:
			a_sum+=1
	print(a_sum)