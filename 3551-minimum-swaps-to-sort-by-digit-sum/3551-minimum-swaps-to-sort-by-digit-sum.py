class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        arr = sorted(nums, key=lambda x: (sum(map(int, str(x))), x))

        pos = {val: i for i, val in enumerate(nums)}
        visited = [False] * len(nums)
        swaps = 0

        for i in range(len(nums)):
            if visited[i] or pos[arr[i]] == i:
                continue

            cycle = 0
            j = i

            while not visited[j]:
                visited[j] = True
                j = pos[arr[j]]
                cycle += 1

            swaps += cycle - 1

        return swaps