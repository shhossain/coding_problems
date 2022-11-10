from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums3 = [0] * (m+n)

        i,j = 0,0
        k = 0
        while i<m and j<n:
            if nums1[i] < nums2[j]:
                nums3[k] = nums1[i]
                k+=1
                i+=1
            else:
                nums3[k] = nums2[j]
                k+=1
                j+=1


        while i<m:
            nums3[k] = nums1[i]
            k+=1
            i+=1

        while j<n:
            nums3[k] = nums2[j]
            k+=1
            j+=1

        for i in range(m+n):
            nums1[i] = nums3[i]

        return nums1







a = [1,2,3,0,0,0]
m = 3
b = [2,5,6]
n = 3
print(Solution().merge(a,m,b,n))                
