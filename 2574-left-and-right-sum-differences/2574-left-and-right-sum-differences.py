class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            res.append(abs(sum(nums[0:i])-sum(nums[i+1:len(nums)])))
        
        return res