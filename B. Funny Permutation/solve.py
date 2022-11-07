def print_arr(arr):
	for i in arr:
		print(i,end=" ")
	print()

for _ in range(int(input())):
	n = int(input())

	if n%2 == 0:
		a = reversed([i for i in range(1,n+1)])
		print_arr(a)
	else:
		if n == 3:
			print(-1)
		else:
			mid = n//2
			a = list(reversed([i for i in range(1,n+1)]))
			a1 = list(reversed(a[:mid+1]))
			a2 = a[mid+1:]
			print_arr(a1+a2)


