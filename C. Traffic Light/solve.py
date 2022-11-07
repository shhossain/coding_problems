def lb(arr,t):
	s = 0
	e= len(arr) - 1
	ans = -1
	while s<= e:
		mid = (s+e)//2
		if arr[mid] < t:
			s = mid+1
		else:
			e = mid-1
			ans = mid
	return ans




for _ in range(int(input())):
	n,target = input().split()
	s = input()
	g = []
	t = []
	for n,i in enumerate(s):
		if i == "g":
			g.append(n)
		elif i == target:
			t.append(n)
	g.append(g[0]+len(s))

	v = 0
	for i in t:
		a = g[lb(g,i)] - i
		if a > v:
			v = a
		
	print(v)
	
