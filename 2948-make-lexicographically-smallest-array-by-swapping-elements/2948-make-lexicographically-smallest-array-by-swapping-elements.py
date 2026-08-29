class Solution:
    def lexicographicallySmallestArray(self, nums, limit):
        arr = sorted((x, i) for i, x in enumerate(nums))
        ans = nums[:]

        i = 0

        while i < len(arr):
            j = i

            while j + 1 < len(arr) and arr[j + 1][0] - arr[j][0] <= limit:
                j += 1

            values = [arr[k][0] for k in range(i, j + 1)]
            indices = sorted(arr[k][1] for k in range(i, j + 1))

            for idx, value in zip(indices, values):
                ans[idx] = value

            i = j + 1

        return ans