class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        val = 0
        for k in range(len(nums)):
            i = 0
            j = k
            while j < len(nums):
                val += len(set(nums[i:j+1])) ** 2
                i+=1
                j+=1
        return val