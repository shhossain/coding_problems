def binary_search(arr,n):
	start = 0
	end = len(arr) - 1
	while start<=end:
		mid = (start+end)//2
		if  arr[mid] == n:
			return mid
		elif arr[mid] < n:
			start = mid + 1
		elif arr[mid] > n:
			end = mid - 1
	
	return -1

def binary_search_unsorted(arr,n):
	arr_map = {j:i for i,j in enumerate(arr)}
	arr_index = [i for i in range(0,len(arr))]
	sorted_arr = sorted(arr)
	s = binary_search(sorted_arr,n)
	if s != -1:
		return arr_map[sorted_arr[s]]
	else:
		return -1

n = int(input())
a = list(map(int,input().split()))
print(binary_search(a,n))
# print(binary_search_unsorted(a,n))
# print(a.index(n))