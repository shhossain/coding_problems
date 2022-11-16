for _ in range(int(input())):
	n = int(input())
	s = input()

	arr = []
	for i in range(n):
		if s[i] == "L":
			arr.append(i)
		else:
			arr.append(n-(i+1))

	asum = sum(arr)
	tsum = asum

	i = 0
	s = 0
	e = n - 1
	ans = []
	while s <= e and s < n and e < n:
		idx = 0
		if i&1 == 1:
			vr = n - (s+1)
			vl = s
			idx = s
			s+=1
		else:
			vr = n - (e+1)
			vl = e
			idx = e
			e-=1

		v = max(vr,vl)
		t = arr[idx]
		arr[idx] = v
		csum = asum
		asum+=(v-t)
		i+=1
		if csum < asum:
			ans.append(asum)

	if len(ans) == 0:
		ans = [asum]


	diff = n - len(ans)
	for i in range(diff):
		ans.append(ans[-1])



	for i in ans:
		print(i,end=" ")
	print()

		


