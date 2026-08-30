class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = s.strip().split(" ")[-1]
        return (len(res))