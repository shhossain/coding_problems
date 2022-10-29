t = int(input())
for _ in range(t):
	n = int(input())
	s = list(map(int,input()))
	cluster = False
	c = 0
	total = 0
	for j,i in enumerate(s):
		if i == 1:
			c = j + 1
		if i == 1 and not cluster:
			total+=1
			cluster = True
		elif i == 0:
			cluster = False
	if c == n:
		total -=1
	print(total)
