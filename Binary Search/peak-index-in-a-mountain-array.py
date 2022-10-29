class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        s = 0
        e = len(arr) -1
        while(s<e):
            mid = (s+e)//2
            if (arr[mid] < arr[mid+1]):
                s = mid + 1
            else:
                e = mid
        return s