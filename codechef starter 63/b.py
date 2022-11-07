for _ in range(int(input())):
	x,y,z = map(int, input().split())
	v = y//z
	if v != y/z:
		v +=1
	print(int(v*x))
