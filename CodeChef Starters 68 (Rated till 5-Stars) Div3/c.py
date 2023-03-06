for _ in range(int(input())):
	n,x,c = map(int, input().split())
	a = list(map(int, input().split()))
	a = sorted(a)

	v = sum(a) - 0
	t = c
	for i in range(n):
		if a[i] != x:
			a[i] = x
			sm = sum(a)
			val = sm - t
			v = max(v,val)
			t+=c
	print(v)