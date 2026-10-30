class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            leftSum = rightSum = 0
            for j in range(0,i):
                leftSum += nums[j]
            for k in range(i+1,len(nums)):
                rightSum += nums[k]
            res.append(abs(leftSum-rightSum))
        
        return res