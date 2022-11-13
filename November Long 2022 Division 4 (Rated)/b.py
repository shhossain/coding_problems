for _ in range(int(input())):
	a,b,x,y = map(int,input().split())

	v = b-a

	flag = False
	if v >= 0:
		if v <= x:
			flag = True
	else:
		v = abs(v)
		if v <= y:
			flag = True


	if flag:
		print("YES")
	else:
		print("NO")
