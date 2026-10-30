class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        totalSum = sum(nums)
        leftSum = 0
        res = []
        for num in nums:
            rightSum = totalSum - leftSum - num
            res.append(abs(leftSum - rightSum))
            leftSum += num
        return res