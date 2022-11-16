from collections import defaultdict



for _ in range(int(input())):
	n,k = map(int, input().split())
	s = list(map(int, input().split()))
	qm = list(map(int, input().split()))
	q = sorted(qm)

	ssum = 0
	i = 0
	ans = defaultdict(lambda:-1)
	for j in range(k):
		while i < n:
			if s[i] <= q[j]:
				ssum+=s[i]
				ans[q[j]] = ssum
				i+=1
			else:
				ans[q[j]] = ssum
				break

	for i in qm:
		v = ans[i]
		if v == -1:
			v = ssum
		print(v,end=" ")
	print()