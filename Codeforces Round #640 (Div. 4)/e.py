for _ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	a_max = max(a)

	ans = [0] * 8001

	for i in range(n):
		s = a[i]
		for j in range(i+1,n):
			s+=a[j]

			if s > a_max or s > 8001:
				break

			ans[s] = 1


	an = 0
	for i in a:
		if ans[i] == 1:
			an+=1
	# print(ans)
	print(an)