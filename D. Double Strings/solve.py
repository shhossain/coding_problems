from collections import defaultdict


for _ in range(int(input())):
	n = int(input())
	m = {}
	m = defaultdict(lambda:-1,m)
	a = []
	for i in range(n):
		s = input()
		m[s]+=1
		a.append(s)
	

	s = ["0"] * n
	for i in range(n):
		for j in range(len(a[i])):
			x,y = a[i][:j],a[i][j:]
			if m[x] != -1 and m[y] != -1:
				s[i]="1"
	print("".join(s))


