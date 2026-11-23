class Solution:
    def checkString(self, s: str) -> bool:
        a = b = None
        for i in range(len(s)):
            if not b and s[i] == "b":
                b = i
            elif s[i] == "a":
                a = i
        return True if a is None or b is None or a<b else False