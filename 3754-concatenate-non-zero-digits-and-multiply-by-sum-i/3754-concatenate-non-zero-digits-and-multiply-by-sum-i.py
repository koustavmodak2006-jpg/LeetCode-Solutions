class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = res = 0 
        for i in str(n):
            if int(i) != 0:
                x+=int(i)
                res=res*10+int(i)
        res*=x
        return res