from collections import Counter, defaultdict

for _ in range(int(input())):
	n,k = map(int,input().split())
	s = input()
	c = Counter(s)
	d = defaultdict(int,c)
	diff = {}
	ct = 0
	marked = defaultdict(int)
	for i in c:
		if marked[i.lower()] != 0:
			continue
		if i.islower():
			diff[i] = abs(d[i.upper()] - d[i])
			ct += min(d[i.upper()], d[i])
			marked[i] = 1
		elif i.isupper():
			diff[i] = abs(d[i.lower()] - d[i])
			ct += min(d[i.lower()], d[i])
			marked[i.lower()] = 1
	keys = list(diff.keys())
	i = 0
	total = 0
	while k:
		try:
			key = keys[i]
		except IndexError:
			break
		if diff[key] >= 2:
			diff[key] -= 2
			ct += 1
			k -= 1
		else:
			i += 1

	print(ct)

