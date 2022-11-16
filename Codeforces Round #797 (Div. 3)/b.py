for _ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	b = list(map(int, input().split()))

	val = a[0] - b[0]
	flag = True
	if val < 0:
		flag = False
	else:
		for i in range(n):
			v = a[i] - val
			if v < 0:
				v = 0
			a[i] = v


		if a!=b:
			flag = False


	if flag:
		print("YES")
	else:
		print("NO")

	