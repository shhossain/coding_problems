for _ in range(int(input())):
	a,c = map(int, input().split())

	v = -1
	for i in range(a,c+1):
		if abs(a-i) == abs(c-i):
			v = i
	print(v)