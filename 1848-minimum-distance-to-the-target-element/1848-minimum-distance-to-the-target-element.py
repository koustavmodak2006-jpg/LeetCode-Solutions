class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        res = []
        for i,j in enumerate(nums):
            if j ==target:
                res.append(abs(i - start))
        return(min(res))