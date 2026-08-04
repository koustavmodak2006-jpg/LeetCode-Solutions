class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums_set = set(nums)
        start,end,res = min(nums),max(nums),[]
        for i in range(start,end+1):
            if i not in nums_set:
                res.append(i)
        return res