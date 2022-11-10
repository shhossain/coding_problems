for _ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))

	# even in even index
	ee = 0
	# odd in even index
	eo = 0
	# even in odd index
	oe = 0
	# odd in odd index
	oo = 0
	for i in range(1, n+1):
		if i % 2 == 0:
			if a[i-1] % 2 == 0:
				ee += 1
			else:
				eo += 1
		else:
			if a[i-1] % 2 == 0:
				oe += 1
			else:
				oo += 1

	if eo == 0:
		eo = ee
		ee = 0

	if oo == 0:
		oo = oe
		oe = 0

	if ee == 0 and oe == 0:
		print("YES")
	else:
		print("NO")
