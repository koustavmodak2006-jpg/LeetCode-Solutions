class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        res = []

        def backtrack(start, current):
            if len(current) == k:
                res.append(current.copy())
                return

            for i in range(start, n + 1):
                current.append(i)
                backtrack(i + 1, current)
                current.pop()

        backtrack(1, [])

        return res