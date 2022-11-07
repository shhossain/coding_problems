for _ in range(int(input())):
	n = int(input())
	ans = 0
	heights = []
	for i in range(n):
		a,b = map(int, input().split())
		if b>a:
			a,b = b,a
		ans+=b
		heights.append(a)

	ans = ans * 2

	heights.sort()
	for i in range(1,n):
		ans+=heights[i] - heights[i-1]

	ans+= heights[0] + heights[n-1]
	print(ans)
