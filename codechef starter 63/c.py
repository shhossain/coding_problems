from math import sqrt

for _ in range(int(input())):
	n = int(input())

	arr = [n]
	for i in range(1,n):
		arr.append(i)

	sq = sqrt(n)
	if sq == int(sq):
		arr[1],arr[2] = arr[2],arr[1]

	for i in arr:
		print(i,end=" ")
	print()
