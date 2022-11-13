for _ in range(int(input())):
	n = input()
	a = list(map(int, input().split()))
	l = sum(a)
	v = (l * (l-1))%998244353
	print(v)


