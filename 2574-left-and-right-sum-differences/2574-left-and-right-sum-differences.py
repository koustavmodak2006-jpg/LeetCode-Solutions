class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            leftSum = sum(nums[0:i])
            rightSum = sum(nums[i+1:len(nums)])
            res.append(abs(leftSum-rightSum))
        
        return res