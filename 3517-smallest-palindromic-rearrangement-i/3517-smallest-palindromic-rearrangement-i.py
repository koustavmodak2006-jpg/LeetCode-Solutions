class Solution:
    def smallestPalindrome(self, s: str) -> str:
        initial = []
        res = ""
        if len(s) %2 != 0:
            odd = len(s) // 2
            for i in range(odd):
                initial += s[i]
            final = sorted(initial)
            res+="".join(final)
            res+=s[odd]
            res+="".join(reversed(final))
            return res
        else:
            even = len(s)//2
            for i in range(even):
                initial+=s[i]
            final = sorted(initial)
            res += "".join(final)
            res += "".join(reversed(final))
            return res