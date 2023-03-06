from collections import defaultdict

for _ in range(int(input())):
	n = int(input())
	s = input()

	m = defaultdict(0)
	v = 0
	c = ""
	for i in s:
		m[i]+=1

		if m[i] > v:
			v = m[i]
			c = i

	if v == n:
		print(n-1)
		continue
	else:
		


