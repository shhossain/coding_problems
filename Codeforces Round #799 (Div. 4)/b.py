


for _ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))

	a_set = set(a)

	ans = len(a_set)
	
	posiable = False
	s = n
	for i in range(n//2):
		if s-2 == ans:
			posiable = True
		else:
			s = s-2

	if not posiable and n != ans:
		ans -= 1

	print(ans)




