class Solution:
    def checkDivisibility(self, n: int) -> bool:
        sum = 0
        prod = 1
        for i in str(n):
            sum += int(i)
            prod *= int(i)
        res = sum + prod

        return True if n % res == 0 else False