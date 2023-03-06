for _ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))

	o = 0
	e = 0
	for i in a:
		if i&1:
			o+=1
		else:
			e+=1

	s = sum(a)
	flag = False
	if n == 2 and o == 2:
		flag = True
	elif not s&1 and o!=n and e!=n:
		flag = True

	if flag:
		print("YES")
	else:
		print("NO")