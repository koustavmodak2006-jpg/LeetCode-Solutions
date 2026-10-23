class Solution:
    def minElement(self, nums: List[int]) -> int:
        res = []
        for i in nums:
            temp = 0
            for j in str(i):
                temp += int(j)
            res.append(temp)
        return min(res)