class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        val = 0
        for k in range(len(nums)):
            i = 0
            for j in range(k,len(nums)):
                val += len(set(nums[i:j+1])) ** 2
                i+=1
        return val