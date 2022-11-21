from collections import defaultdict


for _ in range(int(input())):
	n = int(input())
	s = input()

	m = defaultdict(list)
	for i in range(n):
		m[s[i]].append(i)


	flag = True
	for v in m.values():
		f = True
		for i in range(len(v)-1):
			if v[i+1] - v[i] != 1:
				f = False
				flag = False
				break

		if not f:
			break


	if flag:
		print("YES")
	else:
		print("NO")


