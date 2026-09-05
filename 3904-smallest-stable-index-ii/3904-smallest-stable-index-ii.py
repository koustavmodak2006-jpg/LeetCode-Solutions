class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)

        # right[i] = minimum element from i to n-1
        right = [nums[-1]] * n

        for i in range(n - 2, -1, -1):
            right[i] = min(right[i + 1], nums[i])

        # left = maximum element from 0 to i
        left = 0

        for i in range(n):
            left = max(left, nums[i])

            # instability score
            if left - right[i] <= k:
                return i

        return -1