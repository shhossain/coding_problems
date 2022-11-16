for _ in range(int(input())):
	s = input()
	n = len(s)

	arr = s[0]
	x = 0
	for i in range(1,n,2):
		arr+=s[i]


	print("".join(arr))