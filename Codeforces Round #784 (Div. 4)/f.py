from collections import defaultdict


for _ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))

	m = defaultdict(int)

	ans = 0
	f = 0
	for x,i in enumerate(a):
		f+=i
		m[f] = x+1
	

	i = n - 1
	b = 0
	while i >= 0:
		b+=a[i]

		if m[b]>0 and m[b]<i+1:
			v = m[b] + (n-i)
			ans = max(ans,v)

		i-=1


	print(ans)

	
# Time 1h 10 min
# Seen (partially)
# Correct about prefix and suffix sum
