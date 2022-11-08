def p(x,y):
	return x,y

def px(s):
	return s[0]

def py(s):
	return s[1]

for _ in range(int(input())):
	n,m = map(int, input().split())

	points = {}
	for i in range(1,n+1):
		s = input().split()
		for j in range(1,m+1):
			points[p(j,i)] = int(s[j-1])

	# print(points)


	
	max_point = 0
	for k in points:

		tr = 0
		cp = k
		while px(cp) <= m and py(cp) != 0:
			tr += points[cp]

			x,y = px(cp),py(cp)
			x+=1
			y-=1
			cp = p(x,y)



		tl = 0
		cp = k
		while px(cp) != 0 and py(cp) != 0:
			tl+= points[cp]

			x,y = px(cp),py(cp)
			x-=1
			y-=1
			cp = p(x,y)

		


		br = 0
		cp = k
		while px(cp) <= m and py(cp) <= n:
			br+= points[cp]

			x,y = px(cp),py(cp)
			x+=1
			y+=1
			cp = p(x,y)



		bl = 0
		cp = k
		while px(cp) != 0 and py(cp) <= n:
			bl+= points[cp]

			x,y = px(cp),py(cp)
			x-=1
			y+=1
			cp = p(x,y)


		t = tr+tl+br+bl - (3*points[k])
		
		max_point = max(max_point,t)

	print(max_point)
	




		

	
