def maxSubarraySum(nums: list, k: int) -> int:
    left = 0
    res = 0
    sum = 0
    map = set()
    for right in range(len(nums)):
        while left < right and (nums[right] in map or len(map) >= k):
            sum -= nums[left]
            map.remove(nums[left])
            left += 1
        sum += nums[right]
        map.add(nums[right])
        if len(map) == k:
            res = max(res, sum)
    return res


if __name__ == "__main__":
    a = [1,5,4,2,9,9,9]
    k = 3
    print(maxSubarraySum(a, k))
