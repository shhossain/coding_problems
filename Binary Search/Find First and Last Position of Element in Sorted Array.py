def first(arr,n):
	start = 0
	end = len(arr) - 1
	ans = - 1 
	while start<=end:
		mid = (start+end)//2
		if  arr[mid] == n:
			ans = mid
			end = mid - 1
		elif arr[mid] < n:
			start = mid + 1
		elif arr[mid] > n:
			end = mid - 1
	
	return ans

def last(arr,n):
	start = 0
	end = len(arr) - 1
	ans = -1
	while start <= end:
		mid = (start+end)//2
		if arr[mid] == n:
			ans = mid
			start = mid + 1
		elif arr[mid] < n:
			start = mid + 1
		elif arr[mid] > n:
			end = mid -1
	return ans





class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
    	return [first(nums,target),last(nums,target)]