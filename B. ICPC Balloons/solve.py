for i in range(int(input())):
	n = int(input())
	s = input()

	m = {i:0 for i in s}	
	t = 0
	for i in s:
		if m[i] == 0:
			t+=2
			m[i]+=1
		else:
			t+=1
	print(t)

		

	