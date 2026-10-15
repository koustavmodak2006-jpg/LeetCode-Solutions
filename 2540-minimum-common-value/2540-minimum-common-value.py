class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        if nums1[-1] < nums2[0]:
            return -1
        for i in nums1:
            for j in nums2:
                if j > i:
                    break
                elif i == j:
                    return i
        return -1