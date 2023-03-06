for _ in range(int(input())):
	n,m = map(int, input().split())
	ans = 0
	if n == 2:
		ans = m
	elif n > 2:
		ans = 2 * m
	print(ans)