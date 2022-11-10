def get_ans(arr:list,t:int,n:int):
	s = 0
	e = n - 1
	ans = -1
	while s<=e:
		mid = (s+e)//2
		if arr[mid] >= t:
			ans = mid+1
			e = mid - 1
		else:
			s = mid + 1
	return ans
	


for _ in range(int(input())):
	n,q = map(int, input().split())
	a = list(map(int, input().split()))
	a = sorted(a,reverse=True)


	asum = 0
	prefix_arr = []
	for i in a:
		asum += i 
		prefix_arr.append(asum)


	for i in range(q):
		s = int(input())
		print(get_ans(prefix_arr,s,n))
		

	
