





for _ in range(int(input())):
	a = list(map(int, input().split()))
	ans = 0
	for i in range(1,4):
		if a[i] > a[0]:
			ans+=1
	print(ans)
