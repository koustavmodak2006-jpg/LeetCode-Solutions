class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        res = []
        for i in range(m):
            temp = ""
            for j in range(n):
                if i == 0:
                    temp+="."
                else:
                    if j == n-1:
                        temp+="."
                    else:
                        temp+="#"
            res.append(temp)
        return res