from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        arr = [0] * n
        for i in range(n):
            arr[(i+k)%n] = nums[i]

        nums = [0] * n
        for i in range(n):
            nums[i] = arr[i]

        return nums




print(Solution().rotate([1,2,3,4,5,6,7],3))