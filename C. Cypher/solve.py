




		




for i in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))

	for i in range(n):
		x,s = input().split()
		v = a[i]
		for j in s:
			if j == "D":
				v+=1

				if v==10:
					v = 0
			elif j == "U":
				v-=1

				if v == -1:
					v = 9

		a[i] = v


	for i in a:
		print(i,end=" ")
	print()
