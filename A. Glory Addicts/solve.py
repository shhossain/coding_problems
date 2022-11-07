for _ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	b = list(map(int, input().split()))

	one = 0
	zero = 0
	for i in a:
		if i == 1:
			one+=1
		elif i == 0:
			zero+=1

	print(one, zero)
	b.sort(reverse=True)
	p = 0
	if zero == 0 or one == 0:
		for i in range(n):
			v = b.pop(0)
			p+=v
	elif zero < one:
		for i in range(zero):
			v = b.pop(0) * 2
			print(v)
			p+=v
	else:
		for i in range(one):
			v = b.pop(0) * 2
			p+=v

	for i in b:
		p+=i

	print(p)




	 



	