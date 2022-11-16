for _ in range(int(input())):
	n = int(input())
	s = input()

	ip = s.split("W")
	
	wsp = []
	for i in  ip:
		if i:
			wsp.append(i)

	if not wsp:
		print("YES")
		continue

	flag = True
	for i in wsp:
		a = [0,0]
		for j in i:
			if j == "B":
				a[0] = 1
			if j == "R":
				a[1] = 1
		if sum(a) != 2:
			flag = False
			break


	if flag:
		print("YES")
	else:
		print("NO")


# Time taken 1H 2MIN 
# Rating 1100