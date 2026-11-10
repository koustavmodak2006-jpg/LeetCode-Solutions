class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        limit = len(nums)
        sum = 0
        for i in range(len(nums)):
            if not limit % (i+1):
                sum += nums[i]**2
        return sum