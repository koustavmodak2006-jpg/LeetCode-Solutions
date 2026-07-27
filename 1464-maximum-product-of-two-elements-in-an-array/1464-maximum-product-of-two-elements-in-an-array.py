class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = 1
        for _ in range(2):
            i = max(nums)
            res *= i-1
            nums.remove(i)
        return res