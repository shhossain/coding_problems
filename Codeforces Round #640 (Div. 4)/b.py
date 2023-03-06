for _ in range(int(input())):
	n,k = map(int, input().split())
	
	flag = False
	one = True

	v1 = (1+n-k)
	v2 = (2+n-(2*k))
	if v1 & 1 and v1 > 0:
		flag = True
		one = True

	elif not v2 & 1 and v2 > 0:
		flag = True
		one = False

	if not flag:
		print("NO")
	else:
		v = v2
		s = 2
		if one:
			v = v1
			s = 1

		print("YES")
		print(v,end=" ")
		for i in range(k-1):
			print(s,end=" ")
		print()


