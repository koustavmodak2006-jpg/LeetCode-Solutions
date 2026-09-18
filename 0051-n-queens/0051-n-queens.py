class Solution:

    def initialize(self, n):
        self.board = {}

        for key in ["queen", "row", "col", "nwtose", "swtone"]:
            self.board[key] = {}

        for i in range(n):
            self.board["queen"][i] = -1
            self.board["row"][i] = 0
            self.board["col"][i] = 0

        for i in range(-(n - 1), n):
            self.board["nwtose"][i] = 0

        for i in range(2 * n - 1):
            self.board["swtone"][i] = 0

    def free(self, i, j):
        return (
            self.board["row"][i] == 0
            and self.board["col"][j] == 0
            and self.board["nwtose"][j - i] == 0
            and self.board["swtone"][i + j] == 0
        )

    def addqueen(self, i, j):
        self.board["queen"][i] = j
        self.board["row"][i] = 1
        self.board["col"][j] = 1
        self.board["nwtose"][j - i] = 1
        self.board["swtone"][i + j] = 1

    def undoqueen(self, i, j):
        self.board["queen"][i] = -1
        self.board["row"][i] = 0
        self.board["col"][j] = 0
        self.board["nwtose"][j - i] = 0
        self.board["swtone"][i + j] = 0

    def placequeen(self, i, n, result):
        for j in range(n):

            if self.free(i, j):
                self.addqueen(i, j)

                if i == n - 1:
                    board = []

                    for row in range(n):
                        s = "." * self.board["queen"][row]
                        s += "Q"
                        s += "." * (n - self.board["queen"][row] - 1)
                        board.append(s)

                    result.append(board)

                else:
                    self.placequeen(i + 1, n, result)

                self.undoqueen(i, j)

    def solveNQueens(self, n: int) -> list[list[str]]:
        result = []

        self.initialize(n)

        self.placequeen(0, n, result)

        return result