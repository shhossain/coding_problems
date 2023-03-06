for _ in range(int(input())):
	n = int(input())
	s1 = input()
	s2 = input()
	t = 0
	it = 0
	for i in range(n):
		if s2[i] == "1":
			t += (i+1)
			it += 1


	ans = 0
	for i in range(1, n+1):
		if s1[i-1] == "1":
			val = i * it
			total = t
			if s2[i-1] == "1":
				total -= i
				val -= i
			
			v = abs(total-val)
			ans+=v
			print(i,total,val)


	print(ans)
