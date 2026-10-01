class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        value = {}
        max_count = 0
        majority = 0

        for num in nums:
            value[num] = value.get(num, 0) + 1

            if value[num] > max_count:
                max_count = value[num]
                majority = num

        return majority