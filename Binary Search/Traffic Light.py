for _ in range(int(input())):
	a = input().split()
	n,c = int(a[0]),a[1]
	lights = list(input())

	greens = []
	cs = []
	for i in range(len(lights)):
		if lights[i] == "g":
			greens.append(i)
		elif lights[i] == c:
			cs.append(i)

	print(greens,cs)

	max_dis = 0
	for g in greens:
		for s in cs:
			v = g - s
			if v < 0:
				v = (n-s) + g
			# print(n,s,g,v)

			if v > max_dis:
				print("g",g)
				max_dis = v

	print(max_dis)