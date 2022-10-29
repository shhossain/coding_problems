t= int(input())
for _ in range(t):
	n,x,y = map(int,input().split())
	a = False
	for i in range(0,n+1):
		if i*x == y:
			print("YES")
			a = True
			break

	if not a:
		print("NO")
