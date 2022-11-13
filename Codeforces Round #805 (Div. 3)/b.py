from collections import defaultdict


for _ in range(int(input())):
	s = input()
	n = len(s)
	
	m = defaultdict(int)
	ans = 0
	k = 0
	i = 0
	while i < n:
		if m[s[i]] == 0:
			m[s[i]]=1
			k+=1

		if k == 4:
			ans+=1
			k = 0
			m.clear()
			i-=1

		i+=1

	if k <= 3:
		ans+=1
		k -= 3

	if k < 0:
		k = 0

	print(ans+k)

