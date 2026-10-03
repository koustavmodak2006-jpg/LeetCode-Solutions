class Solution:
    def numOfStrings(self, patterns: list[str], word: str) -> int:
        count=0
        for letters in patterns:
            if letters in word:
                count+=1
        return count