class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        start,end,res = min(nums),max(nums),[]
        for i in range(start,end+1):
            if i not in nums:
                res.append(i)
        return res