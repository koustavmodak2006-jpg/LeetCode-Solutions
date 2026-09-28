class Solution:
    def maxDepth(self, s: str) -> int:
        ls = []
        count = 0
        for i in s:
            if i == ")":
                count = max(count,len(ls))
                ls.pop()
            else:
                if i == "(":
                    ls.append(i)
        return count