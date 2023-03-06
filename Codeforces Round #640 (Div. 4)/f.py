for _ in range(int(input())):
	n0,n1,n2 = map(int, input().split())

	if n0 and n1==0 and n2==0:
		print("0"*(n0+1))
		continue
	elif n2 and n1==0 and n0==0:
		print("1" * (n2+1))
	elif n1 and n2==0 and n0==0:
		c = "0"
		for i in range(n1):
			if c[-1] == "0":
				c+="1"
			else:
				c+="0"
		print(c)

	else:
		s = ""
		if n0 > 0:
			s = "0" * (n0 + 1)

			if n1 > 0 and n2 > 0:
				n1-=1

		if n2 > 0:
			for i in range(n2+1):
				s+="1"

		for i in range(n1):
			if s[-1] == "0":
				s+="1"
			else:
				s+="0"
		print(s)


		

		
		

			

