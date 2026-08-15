class Solution:
    def longestSubsequence(self, nums):
        xor = 0

        for x in nums:
            xor ^= x

        # Entire array has non-zero XOR
        if xor != 0:
            return len(nums)

        # XOR is zero, remove one non-zero element
        for x in nums:
            if x != 0:
                return len(nums) - 1

        # All elements are zero
        return 0