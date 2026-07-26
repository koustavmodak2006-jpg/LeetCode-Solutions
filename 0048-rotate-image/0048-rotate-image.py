class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        index = 0
        count = 0
        initial = []
        res = []

        while count <= len(matrix)-1:
            if index <= len(matrix)-1:
                initial.append(matrix[index][count])
                index+=1
            else:
                initial.reverse()
                res.append(initial.copy())

                initial.clear()
                index = 0
                count+=1
        matrix[:] = res
        return