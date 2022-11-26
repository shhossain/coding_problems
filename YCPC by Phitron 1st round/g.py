a,b = map(int, input().split())
if a > b:
	print("Argentina")
elif a < b:
	print("Brazil")
else:
	while 1:
		s1 = input()
		s2 = input()
		a,b = 0,0
		for i,j in zip(s1,s2):
			if i == "1":
				a+=1
			if j == "1":
				b+=1

		if a != b:
			break

	if a > b:
		print("Argentina")
	elif a < b:
		print("Brazil")



