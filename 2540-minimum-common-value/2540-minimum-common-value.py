class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        for i in nums1:
            for j in nums2:
                if j > i:
                    break
                elif i == j:
                    return i
        return -1