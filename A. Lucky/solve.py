for _ in range(int(input())):
	s1,s2=0,0
	a = list(map(int, input()))

	for i in range(6):
		if i > 2:
			s2+=a[i]
		else:
			s1+=a[i]

	if s1 == s2:
		print("YES")
	else:
		print("NO")