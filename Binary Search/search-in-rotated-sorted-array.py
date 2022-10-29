
def getPivot(arr):
    s = 0
    e = len(arr) - 1
    while s < e:
        mid = (s+e)//2
        if arr[mid] >= arr[0]:
            s = mid + 1
        else:
            e = mid
    return s

def binary_search(arr,target,s,e):
    # s = 0
    # e = len(arr) -1
    while s<=e:
        mid = (s+e)//2
        if arr[mid] == target:
            return mid
        else if arr[mid] > target:
            e = mid - 1
        else:
            s = mid + 1
    return -1



class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot = getPivot(nums)
        if nums[pivot] == target:
            return pivot
        else if nums[pivot] < target:
            return binary_search(nums,target,pivot+1,len(list)-1)
        else:
            return binary_search(nums,target,0,pivot)
