for x in range(int(input())):
	n,m = map(int, input().split())
	n,m = n*2+1,m*2+1
	print(f"Case #{x+1}:")
	for i in range(1,n+1):
		s = "|"
		d = "."
		if i&1:
			s = "+"
			d = "-"
		for j in range(1,m+1):
			if (i == 1 and j == 1):
				c = "."
			elif (i == 1 and j == 2):
				c = "."
			elif (i == 2 and j ==1):
				c = "."
			elif not j&1:
				c = d
			else:
				c = s

			print(c,end="")
		print()




