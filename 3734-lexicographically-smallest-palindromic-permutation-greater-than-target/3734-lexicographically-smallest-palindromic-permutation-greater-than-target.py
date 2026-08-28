class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:

        n = len(s)

        # -----------------------------------------
        # 1. Count characters
        # -----------------------------------------
        count = [0] * 26

        for ch in s:
            count[ord(ch) - ord('a')] += 1

        # -----------------------------------------
        # 2. Check whether palindrome is possible
        # -----------------------------------------
        odd = 0
        middle = ""

        for i in range(26):
            if count[i] % 2 == 1:
                odd += 1
                middle = chr(ord('a') + i)

        if odd > 1:
            return ""

        # -----------------------------------------
        # 3. Only half of each character is needed
        #    for the left half.
        # -----------------------------------------
        half = [c // 2 for c in count]

        half_len = n // 2

        prefix = []

        # -----------------------------------------
        # Can current prefix be completed into
        # a palindrome > target?
        # -----------------------------------------
        def can_make_greater():

            # Start with our already chosen prefix
            left = prefix[:]

            # Fill remaining positions with the
            # LARGEST possible characters.
            #
            # This creates the largest possible
            # palindrome having this prefix.
            for i in range(25, -1, -1):
                if half[i] > 0:
                    left.extend([chr(ord('a') + i)] * half[i])

            left = ''.join(left)

            # Construct palindrome
            palindrome = left + middle + left[::-1]

            return palindrome > target

        # -----------------------------------------
        # 4. Build left half greedily
        # -----------------------------------------
        for pos in range(half_len):

            found = False

            # Try smallest possible character first
            for i in range(26):

                if half[i] == 0:
                    continue

                # Temporarily use this character
                half[i] -= 1
                prefix.append(chr(ord('a') + i))

                # Is there ANY completion that works?
                if can_make_greater():
                    found = True
                    break

                # This character cannot lead to
                # a valid answer, so undo it.
                prefix.pop()
                half[i] += 1

            if not found:
                return ""

        # -----------------------------------------
        # 5. Construct final palindrome
        # -----------------------------------------
        left = ''.join(prefix)

        answer = left + middle + left[::-1]

        if answer > target:
            return answer

        return ""