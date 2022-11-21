from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
q = int(input())

m = defaultdict(lambda:None)
for i in range(n):
	m[i] = a[i]

val = 0

for i in range(q):
	v = list(map(int, input().split()))

	if v[0] == 3:
		idx = v[1]-1
		mv = m[idx]
		ans = mv
		if mv is None:
			ans = val
		print(ans)
	elif v[0] == 1:
		val = v[1]
		m = defaultdict(lambda: None)
	elif v[0] == 2:
		idx = v[1]-1
		add = v[2]
		mv = m[idx]
		if mv is None:
			add+=val
			m[idx] = add
		else:
			m[idx]+=add


