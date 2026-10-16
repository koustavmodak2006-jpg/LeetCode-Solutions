class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        res = {}
        count = 0
        for i in word:
            res[ord(i)]=i
        for i in res:
            if i+32 in res:
                count +=1
        return count