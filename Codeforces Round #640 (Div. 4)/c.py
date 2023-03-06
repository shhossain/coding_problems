for _ in range(int(input())):
	n,k = map(int, input().split())
	a = n-1
	v = (n*k)//a
	if v%n == 0:
		v-=1
	print(v)
	

	



