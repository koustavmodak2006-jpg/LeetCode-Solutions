class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num:
            return ""

        res = ""

        for _ in range(num):
            digit = min(9, sum)
            res += str(digit)
            sum -= digit

        if sum > 0:
            return ""

        return res