class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = 0
        a = b = c = -1

        for i in range(len(s)):
            if s[i] == 'a':
                a = i
            elif s[i] == 'b':
                b = i
            elif s[i] == 'c':
                c = i

            count += min(a, b, c) + 1

        return count