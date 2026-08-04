class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        start,end,res = nums[0],nums[len(nums)-1],[]
        for i in range(start,end+1):
            if i not in nums:
                res.append(i)
        return res