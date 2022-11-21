for _ in range(int(input())):
	start,end,x, = map(int, input().split())
	a, b = map(int, input().split())


	if a > b:
		a,b = b,a


	ans = -1
	if a==b:
		ans = 0
	
	elif b-a>=x:
		ans = 1
	elif end - b >= x or a - start>= x:
		ans = 2
	elif (end - b < x and b - start >= x) or (a - start < x and b - start>= x): 
		ans = 3


	print(ans)
