class Solution:
    def minimumDeletions(self, nums):
        n = len(nums)

        minIndex = nums.index(min(nums))
        maxIndex = nums.index(max(nums))

        left = min(minIndex, maxIndex)
        right = max(minIndex, maxIndex)

        from_front = right + 1
        from_back = n - left
        from_both = (left + 1) + (n - right)

        return min(from_front, from_back, from_both)