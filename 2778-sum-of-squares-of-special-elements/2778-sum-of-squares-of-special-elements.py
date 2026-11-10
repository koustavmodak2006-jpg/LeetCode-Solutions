class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        limit = len(nums)
        sum = 0
        for i in range(len(nums)):
            if limit % (i+1) == 0:
                sum += nums[i]**2
        return sum