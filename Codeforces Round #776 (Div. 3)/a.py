


for _ in range(int(input())):
	s1 = input()
	s2 = input()
	n = len(s1)
	arr = []

	for i in range(n):
		if s1[i] == s2:
			arr.append(i)

	flag = False
	for i in arr:
		if not i&1 and not (n-i+1)&1:
			flag = True
			break


	if flag:
		print("YES")
	else:
		print("NO")