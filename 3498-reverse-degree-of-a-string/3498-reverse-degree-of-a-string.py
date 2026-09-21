class Solution:
    def reverseDegree(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            res += ((27 - (ord(s[i].lower()) - 96)) * (i+1))
        return res