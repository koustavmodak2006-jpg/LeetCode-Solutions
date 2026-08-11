class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        total = nums[0]
        i = 1

        # Find sum of longest consecutive prefix
        while i < len(nums) and nums[i] == nums[i - 1] + 1:
            total += nums[i]
            i += 1

        # Find smallest integer >= total not present in nums
        while total in nums:
            total += 1

        return total