for _ in range(int(input())):
	n,k = map(int, input().split())
	if k == 1:
		print("Yes")
		continue
	v = n-k
	if v&k == 0 and (v//k)%k ==0:
		print("Yes")
	else:
		print("No")