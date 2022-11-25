for _ in range(int(input())):
	a,b,c = map(int, input().split())
	d = sorted([a,b,c])
	print(d[1])