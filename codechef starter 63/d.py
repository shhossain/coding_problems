def solve(a,b):
	if b > a:
		v = b/a
		if v != int(v):
			v = int(v) + 1
		return v
	elif a > b:
		v = a/b
		if v != int(v):
			v = int(v) + 1
		b = b * v
		return solve(a,b)
	else:
		return a//b


for _ in range(int(input())):
	a,b = map(int, input().split())
	print(int(solve(a,b)))

