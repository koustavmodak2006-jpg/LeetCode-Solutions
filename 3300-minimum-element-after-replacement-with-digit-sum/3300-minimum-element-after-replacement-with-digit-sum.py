class Solution:
    def minElement(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            temp = 0
            for j in str(nums[i]):
                temp += int(j)
            nums[i] = temp
        return min(nums)