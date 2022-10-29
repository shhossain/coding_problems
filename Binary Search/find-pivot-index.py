a = list(map(int,input().split(",")))

left,right = 0, sum(a)

for idx,i in enumerate(a):
	right-= i
	if left == right:
		print(idx)
	left+=i
	


