for _ in range(int(input())):
	a = int(input())
	str_a = str(a)
	n = str_a.count(str_a[0])
	val = (n*(n+1))//2
	first = int(str_a[0])
	print((first-1)*10 + val)