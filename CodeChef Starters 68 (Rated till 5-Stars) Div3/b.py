for _ in range(int(input())):
	n,x = map(int, input().split())
	v = 2**x
	for i in range(n):
		v = v - v//2
	print(v)
