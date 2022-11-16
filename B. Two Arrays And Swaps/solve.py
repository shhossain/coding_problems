for _ in range(int(input())):
	n,k = map(int, input().split())
	a = list(map(int, input().split()))
	b = list(map(int, input().split()))
	a = sorted(a)
	b = sorted(b,reverse=True)


	arr = []
	for i in range(n):
		if i < k:
			arr.append(max(a[i],b[i]))
		else:
			arr.append(a[i])
	print(sum(arr))