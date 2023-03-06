n = int(input())


notes = [500,100,50,10,5,1]
ans =   [0,   0,  0, 0,0,0]
total = 0
for x,note in enumerate(notes):
	re = n - total
	v = re//note
	ans[x] = v
	total+= v * note


# will print in reverse
for n,a in zip(notes[::-1],ans[::-1]): 
	for _ in range(a):
		print(n,end=" ")

