class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def quick_sort(left, right):
            if left >= right:
                return

            pivot = nums[right]
            i = left

            for j in range(left, right):
                if nums[j] <= pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1

            nums[i], nums[right] = nums[right], nums[i]

            quick_sort(left, i - 1)
            quick_sort(i + 1, right)

        quick_sort(0, len(nums) - 1)