class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        res = 1
        for i in str(n):
            res*= int(i)
        if res % t != 0:
            return self.smallestNumber(n=n + 1, t=t)
        else:
            return n