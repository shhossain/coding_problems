




for _ in range(int(input())):
	n,s = map(int, input().split())
	a = list(map(int, input().split()))


	ones = []
	for i in range(n):
		if a[i] == 1:
			ones.append(i)

	len_one = len(ones)


	a_sum = sum(a)

	if a_sum == s:
		print(0)
		continue
	elif a_sum < s:
		print(-1)
		continue


	one_index = []
	e = 0
	o = 1e10
	lo = 0
	ro = 0
	for i in range(n):
		if a[i] == 1:
			one_index.append(i)



		if e == s:
			if i+1 > len_one:
				v = n+1
			else:
				v = ones[i+1]

			ro = n - v - 1
			print(ro)

			e-=1
		
		e+=a[i]

	


			
