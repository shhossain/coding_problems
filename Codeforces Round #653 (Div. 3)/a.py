for _ in range(int(input())):
	x,y,n = map(int, input().split())

	v = n%x

	if v != y:
		val = n - v - x + y
	else:
		val = n
	
	if val < 0:
		val = 0

	print(val)
