from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k =  0
        for i in range(n):
            if nums[i] != 0:
                nums[k] = nums[i]
                k+=1

        for i in range(k,n):
            nums[i] = 0

        return nums 



print(Solution().moveZeroes([0,1,0,0,3,12,0,34]))