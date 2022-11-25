def inversions(arr):
	s = 0
	ans = 0
	for i in arr:
		if i == 1:
			s+=1
		else:
			ans+=s
	return ans

for _ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	v1 = inversions(a)
	
	a2 = []
	flag = True
	for i in range(n):
		v = a[i]
		if v == 0 and flag:
			v = 1
			flag = False
		a2.append(v)

	a3 = []
	i = n
	flag = True
	while i > 0:
		i-=1
		v = a[i]
		if v == 1 and flag:
			v = 0
			flag = False
		a3.append(v)

	a3 = a3[::-1]

	v2,v3 = inversions(a2),inversions(a3)
	print(max(v1,v2,v3))

