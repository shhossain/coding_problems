from collections import defaultdict


for _ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	m = {}
	m = defaultdict(lambda:0,m)
	for i in a:
		m[i]+=1

	p = n
	for i in range(n):

		if m[a[i]]-1 != 0:
			p = n - (i+1)
			m[a[i]] -= 1

	print(n-p)