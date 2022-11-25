M = 10**10

for _ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))

	arr = [a[0]]
	c = a[0]
	for i in range(1,n):
		if a[i] != c:
			c = a[i]
			arr.append(c)



	arr_len = len(arr)
	valley = 0
	for i in range(arr_len):
		if i == 0:
			v1 = M
		else:
			v1 = arr[i-1]

		if i == arr_len - 1:
			v3 = M
		else:
			v3 = arr[i+1]

		v2 = arr[i]
		

		if v1 > v2 < v3:
			valley += 1

		# print(i,v1,v2,v3,valley)



		
	if valley == 1:
		print("YES")
	else:
		print("NO")

	