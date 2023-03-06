def printPascal(n:int):
	arr = [[1]]
	for i in range(n-1):
		sarr = [1]
		j = 1
		while j < len(arr[i]):
			sarr.append(arr[i][j] + arr[i][j-1])
			j+=1
		sarr.append(1)
		arr.append(sarr)

	return arr


v = printPascal(5)
for i in v:
	print(*i)