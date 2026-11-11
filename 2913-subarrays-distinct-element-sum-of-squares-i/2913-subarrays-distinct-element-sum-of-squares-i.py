class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        res = []
        val = 0
        for k in range(len(nums)):
            i = 0
            j = k
            while j < len(nums):
                res.append(nums[i:j+1])
                i+=1
                j+=1
        for i in res:
            val += len(set(i)) **2
        return val