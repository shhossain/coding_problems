from collections import defaultdict


for _ in range(int(input())):
	x = input()
	if not x:
		x = input()
	if not x:
		x = input()
		


	n,q = map(int, x.split())
	a = list(map(int, input().split()))

	m = defaultdict(list)
	for i in range(n):
		m[a[i]].append(i)


	# print(m)
	for i in range(q):
		a,b = map(int, input().split())
		
		v1 = m[a]
		v2 = m[b]

		if not v1 or not v2:
			print("NO")
			continue

		v1 = v1[0]
		v2 = v2[-1]

		if v2 > v1:
			print("YES")
		else:
			print("NO")
