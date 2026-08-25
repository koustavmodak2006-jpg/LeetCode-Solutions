class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        for i in range(1,102):
            res = k * i
            if res not in nums:
                return res
                