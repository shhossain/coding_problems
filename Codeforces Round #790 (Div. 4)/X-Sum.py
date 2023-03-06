def right_down(arr,n,m,i,j):
	s = 0
	while i < n and j < m:
		s += arr[i][j]
		i+=1
		j+=1
	return s

def left_down(arr,n,m,i,j):
	s = 0
	while i < n and j > -1:
		s += arr[i][j]
		i+=1
		j-=1
	return s

def right_up(arr,n,m,i,j):
	s = 0
	while i > -1 and j < m:
		s += arr[i][j]
		i-=1
		j+=1
	return s

def left_up(arr,n,m,i,j):
	s = 0
	while i > -1 and j > -1:
		s += arr[i][j]
		i-=1
		j-=1
	return s



for _ in range(int(input())):
	n,m = map(int,input().split())

	arr = []
	for i in range(n):
		a = list(map(int, input().split()))
		arr.append(a)


	best = 0
	bi,bi = 0,0
	for i in range(n):
		for j in range(m):
			b = right_down(arr,n,m,i,j) + right_up(arr,n,m,i,j) + left_down(arr,n,m,i,j) + left_up(arr,n,m,i,j) - (3*(arr[i][j]))

			if b > best:
				bi = i
				bj = j
				best = b
	print(best)
