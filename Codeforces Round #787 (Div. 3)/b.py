for _ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))

	c = a[-1]
	i = n - 2
	flag = True
	ans = 0
	while i >= 0:
		w = a[i]

		o = 0
		while w >= c:
			w = w//2
			o+=1
			if w == 0:
				break

		if c==0 and w==0:
			flag = False
			break

		c = w
		ans+=o
		i-=1

	if not flag:
		ans = -1

	print(ans)

