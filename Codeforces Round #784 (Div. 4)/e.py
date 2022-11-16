from collections import defaultdict


for _ in range(int(input())):
	n = int(input())
	m = defaultdict(int)
	m1 = defaultdict(int)
	m2 = defaultdict(int)

	vs = []
	for i in range(n):
		v = input()
		vs.append(v)
		
	
	ans = 0
	for i in vs:
		v = m1[i[0]] + m2[i[1]] - 2*(m[i])
		m1[i[0]]+=1
		m2[i[1]]+=1
		m[i]+=1
		ans+=v
		

	print(ans)
	
	
