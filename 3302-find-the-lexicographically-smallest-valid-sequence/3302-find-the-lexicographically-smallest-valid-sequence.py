class Solution:
    def validSequence(self, word1: str, word2: str) -> list[int]:
        n, m = len(word1), len(word2)

        # suf[i] = number of characters from word2
        # that can be matched in word1[i:]
        suf = [0] * (n + 1)

        j = m - 1
        for i in range(n - 1, -1, -1):
            if j >= 0 and word1[i] == word2[j]:
                j -= 1
            suf[i] = m - 1 - j

        ans = []
        j = 0
        changed = False

        for i in range(n):
            if j == m:
                break

            # Exact match
            if word1[i] == word2[j]:
                ans.append(i)
                j += 1

            # Use the one allowed mismatch
            elif not changed:
                if suf[i + 1] >= m - j - 1:
                    ans.append(i)
                    j += 1
                    changed = True

        return ans if len(ans) == m else []