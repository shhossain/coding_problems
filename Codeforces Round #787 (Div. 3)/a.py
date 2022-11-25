for _ in range(int(input())):
	a,b,c,x,y = map(int,input().split())
	a1 = x-a
	b1 = y-b

	if a1 < 0:
		a1 = 0
	if b1 < 0:
		b1 = 0
		
	if a1+b1 <= c:
		print("YES")
	else:
		print("NO")