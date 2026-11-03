class Solution:
    def minMoves(self, nums: List[int]) -> int:
        count = 0
        i = max(nums)
        for j in nums:
            count += i-j
        return count