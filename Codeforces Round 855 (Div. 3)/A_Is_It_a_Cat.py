for _ in range(int(input())):
	n = input()
	a = input().lower()
	fs = a[0]
	for i in range(1,len(a)):
		if fs[-1] != a[i]:
			fs += a[i]

	if fs == "meow":
		print("YES")
	else:
		print("NO")
