class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        res = []

        for i in range(m):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    res.append([i,j])
        for x,y in res:
            for i in range(m):
                matrix[i][y] = 0
            for j in range(n):
                matrix[x][j] = 0
        return matrix