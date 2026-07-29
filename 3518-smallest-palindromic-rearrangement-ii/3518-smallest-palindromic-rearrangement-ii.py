class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        cnt = Counter(s)

        freq = [0] * 26
        mid = ""

        for c in cnt:
            if cnt[c] & 1:
                mid = c
            freq[ord(c) - ord('a')] = cnt[c] // 2

        m = sum(freq)

        # factorials
        fact = [1] * (m + 1)
        for i in range(1, m + 1):
            fact[i] = fact[i - 1] * i

        # initial number of distinct half permutations
        ways = fact[m]
        for f in freq:
            ways //= fact[f]

        if ways < k:
            return ""

        ans = []
        remaining = m

        while remaining:
            for i in range(26):
                if freq[i] == 0:
                    continue

                # permutations if we place this character here
                candidate = ways * freq[i] // remaining

                if candidate >= k:
                    ans.append(chr(i + ord('a')))
                    ways = candidate
                    freq[i] -= 1
                    remaining -= 1
                    break
                else:
                    k -= candidate

        left = "".join(ans)
        return left + mid + left[::-1]