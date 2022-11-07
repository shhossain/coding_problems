def point(s):
	p = 0
	a = 1/100
	if s[-1] == "S":
		p = 1000
		a = -a
	elif s[-1] == "M":
		p = 2000
	elif s[-1] == "L":
		p = 3000

	for i in s:
		if i == "X":
			p = p + a
	return p



for i in range(int(input())):
	s1,s2 = input().split()
	ps1,ps2 = point(s1),point(s2)
	if ps1 > ps2:
		print(">")
	elif ps1 < ps2:
		print("<")
	else:
		print("=")