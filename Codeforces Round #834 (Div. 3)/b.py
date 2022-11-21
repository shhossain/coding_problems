for _ in range(int(input())):
	n,s = map(int, input().split())
	a = list(map(int, input().split()))


	m = {}
	for i in range(1,s+1):
		m[i] = 0

	for i in a:
		m[i] = 1


	msum = 0
	flag = False
	for k,v in m.items():
		if v == 0:
			msum += k
			a.append(k)
			if msum == s:
				flag = True
				break

			elif msum > s:
				a.pop()
				break


	asort = sorted(a)

	for i in range(len(asort)-1):
		if asort[i+1] - asort[i] != 1:
			flag = False
			break

			



	if flag:
		print("YES")
	else:
		print("NO")
