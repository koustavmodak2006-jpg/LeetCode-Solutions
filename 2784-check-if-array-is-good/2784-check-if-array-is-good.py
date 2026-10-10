from collections import Counter
class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        if n < 1:
            return False

        counts = Counter(nums)

        # Check that maximum value n appears twice
        if counts[n] != 2:
            return False

        # Check that all elements from 1 to n - 1 appear exactly once
        for i in range(1, n):
            if counts[i] != 1:
                return False

        return True