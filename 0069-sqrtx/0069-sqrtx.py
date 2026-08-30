class Solution:
    def mySqrt(self, x: int) -> int:
        if x >0 and x <=3:
            return 1
        elif x <=0:
            return 0
        res = count = 0
        for i in range(1,x):
            if i%2 !=0:
                res += i
                if res <=x:
                    count+=1
                else:break
        return count