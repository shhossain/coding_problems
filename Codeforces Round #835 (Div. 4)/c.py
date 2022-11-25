for _ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	asort = sorted(a,reverse=True)

	ans_arr = []
	for i in range(n):
		v = a[i]
		m = asort[0]
		if v == asort[0]:
			m = asort[1]

		ans_arr.append(v-m)

	for i in ans_arr:
		print(i,end=" ")
	print()