class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()

        if len(nums1) %2 != 0:
            return nums1[len(nums1)//2]
        else:
            left = len(nums1) // 2
            right = left - 1
            return (nums1[left]+nums1[right])/2