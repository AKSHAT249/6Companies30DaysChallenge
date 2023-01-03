class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        total = sum(nums)
        n = len(nums)
        value = 0
        for i in range(len(nums)):
            value += i*nums[i]
        maximum = value
        for i in range(len(nums)-1,-1,-1):
            value = value+total-n*nums[i]
            maximum = max(maximum , value)
        return maximum
