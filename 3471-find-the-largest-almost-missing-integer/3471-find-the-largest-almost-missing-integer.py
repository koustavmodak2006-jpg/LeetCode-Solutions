class Solution:
    def largestInteger(self, nums, k):
        count_dict = {}

        for i in range(len(nums) - k + 1):
            j, count = i, 0
            seen = set()

            while count < k:
                seen.add(nums[j])

                count += 1
                j += 1

            for num in seen:
                if num not in count_dict:
                    count_dict[num] = 1
                else:
                    count_dict[num] += 1

        max_value = [
            key for key, value in count_dict.items()
            if value == 1
        ]

        return max(max_value) if max_value else -1


sol = Solution()
print(sol.largestInteger(nums=[0, 0], k=1))