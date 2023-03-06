for _ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))

	m = 1
	alice = a[0]
	bob = 0
	i,j= 1,n-1
	aturn = False
	current = a[0]

	while i <= j:
		s = 0
		if m&1: #bob
			for k in range(j,i-1,-1):
				s+=a[k]
				j-=1
				if s > current:
					current = s
					break
			bob+=s
		else:
			for k in range(i,j+1):
				s+=a[k]
				i+=1
				if s > current:
					current = s
					break
			alice+=s
		m+=1
		

	print(m,alice,bob)