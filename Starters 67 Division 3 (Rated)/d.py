for _ in range(int(input())):
	n,k = map(int, input().split())
	n1 = n-1
	s = (n*n1)//2
	if k<n//2:
		t = (n-(2*k))
		t1 = t-1
		s-= (t*t1)//2
	print(s)