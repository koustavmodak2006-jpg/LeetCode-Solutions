class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = 0
        
        b = text.count("b")
        a = text.count("a")
        l = text.count("l")
        o = text.count("o")
        n = text.count("n")
        while b >= 1 and a >= 1 and l>= 2 and o >= 2 and n >= 1:
            b-=1
            a-=1
            n-=1
            l-=2
            o-=2
            count +=1
        
        return count