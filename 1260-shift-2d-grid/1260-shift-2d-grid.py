class Solution:
    def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        n = len(grid)
        m = len(grid[0])

        res = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                new_pos = (i * m + j + k) % (n * m)

                new_i = new_pos // m
                new_j = new_pos % m

                res[new_i][new_j] = grid[i][j]

        return res