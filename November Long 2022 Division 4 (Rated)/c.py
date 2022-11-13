from collections import defaultdict

for _ in range(int(input())):
	n = int(input())
	s = input()

	m = defaultdict(int)

	for i in s:
		m[i]+=1


	flag = True
	for v in m.values():
		if v%2!=0:
			flag = False
			break

	if flag:
		print("YES")
	else:
		print("NO")