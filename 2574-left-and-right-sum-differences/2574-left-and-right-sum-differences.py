class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            leftSum = rightSum = 0
            for j in range(0,len(nums)):
                if j == i:
                    continue
                elif j < i:
                    leftSum += nums[j]
                else:
                    rightSum += nums[j]
            res.append(abs(leftSum-rightSum))
        
        return res