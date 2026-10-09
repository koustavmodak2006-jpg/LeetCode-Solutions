class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        count = 0
        res = ""
        for i in s:
            if i == "(":
                if count > 0:
                    res += i
                count += 1
            else:
                count -= 1
                if count > 0:
                    res += i
        return res