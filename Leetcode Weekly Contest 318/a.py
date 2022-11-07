from typing import List

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] = nums[i]*2
                nums[i+1] = 0


        arr = []
        zero = []
        for i in nums:
            if i == 0:
                zero.append(0)
            else:
                arr.append(i)

        return arr + zero

        



print(Solution().applyOperations([1,2,2,1,1,0]))