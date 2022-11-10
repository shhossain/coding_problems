from collections import defaultdict


for _ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	m = defaultdict(lambda: 0)
	flag = False
	for i in a:
		m[i] += 1

		if m[i] >= 3:
			flag = True
			print(i)
			break

	if not flag:
		print(-1)
