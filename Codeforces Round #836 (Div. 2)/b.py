for _ in range(int(input())):
	n = int(input())
	
	ans = []
	if n&1:
		ans = [3 for i in range(n)]
	else:
		ans = [2 for i in range(n-2)] + [1,3]

	print(*ans)