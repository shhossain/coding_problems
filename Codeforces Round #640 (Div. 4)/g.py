for _ in range(int(input())):
	n = int(input())

	odd = [2*i-1 for i in range(1,n+1) if 2*i-1 <=n][::-1]
	even =[ 2*i for i in range(1,n+1) if 2*i <=   n]
	
	if len(even) < 2:
		print(-1)
		continue

	even[0],even[1] = even[1],even[0]
	print(*odd,*even)
