class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)

        # is_pal[i][j] = True if s[i:j+1] is a palindrome
        is_pal = [[False] * n for _ in range(n)]

        for i in range(n):
            is_pal[i][i] = True

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                if s[i] == s[j] and (length == 2 or is_pal[i + 1][j - 1]):
                    is_pal[i][j] = True

        # dp[i] = maximum number of non-overlapping palindromes
        # using s[0:i]
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            # Don't take a palindrome ending at i-1
            dp[i] = dp[i - 1]

            # Try every palindrome ending at i-1
            for j in range(i):
                if i - j >= k and is_pal[j][i - 1]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return dp[n]