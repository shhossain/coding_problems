for _ in range(int(input())):
	n, m, k, x = map(int, input().split())
	v = x % (n*k + m)
	if v != 0 and (v - n*(k-1)) <= 0:
		print("NO")
	else:
		print("YES")
