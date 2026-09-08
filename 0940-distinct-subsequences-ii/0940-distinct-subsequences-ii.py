class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7

        n = len(s)

        # dp[i] = number of distinct subsequences
        # including the empty subsequence
        dp = [0] * (n + 1)
        dp[0] = 1

        # Last occurrence of each character
        last = [-1] * 26

        for i in range(1, n + 1):
            c = ord(s[i - 1]) - ord('a')

            # Each subsequence can either take or skip
            # the current character
            dp[i] = (2 * dp[i - 1]) % MOD

            # Remove duplicates caused by previous occurrence
            if last[c] != -1:
                dp[i] = (dp[i] - dp[last[c] - 1]) % MOD

            last[c] = i

        # Remove the empty subsequence
        return (dp[n] - 1) % MOD