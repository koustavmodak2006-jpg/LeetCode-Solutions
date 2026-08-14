class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        l = r = 0
        res = 0
        ls = ""
        for r in range(len(s)):
            ls += s[r]

            while ls.count(s[r]) > 2:
                ls = ls[1:]
                l += 1

            res = max(res, r - l + 1)

        return res