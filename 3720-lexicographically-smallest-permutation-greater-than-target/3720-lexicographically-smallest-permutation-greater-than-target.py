class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:

        freq = [0] * 26

        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        n = len(target)

        # Try to keep target as prefix as long as possible
        for i in range(n):

            x = ord(target[i]) - ord('a')

            # If target[i] is available, use it
            if freq[x] > 0:
                freq[x] -= 1
                continue

            # target[i] is not available.
            # Try to put the smallest character > target[i].
            for y in range(x + 1, 26):

                if freq[y] > 0:
                    freq[y] -= 1

                    ans = target[:i] + chr(y + ord('a'))

                    # Put remaining characters in sorted order
                    for k in range(26):
                        ans += chr(k + ord('a')) * freq[k]

                    return ans

            # No bigger character at this position.
            # We must backtrack.
            break

        else:
            # Entire target was matched exactly.
            # But we need STRICTLY greater.
            i = n

        # Backtrack
        for j in range(i - 1, -1, -1):

            x = ord(target[j]) - ord('a')

            # Restore target[j]
            freq[x] += 1

            # Find the smallest character > target[j]
            for y in range(x + 1, 26):

                if freq[y] > 0:

                    freq[y] -= 1

                    ans = target[:j] + chr(y + ord('a'))

                    # Smallest possible suffix
                    for k in range(26):
                        ans += chr(k + ord('a')) * freq[k]

                    return ans

        return ""