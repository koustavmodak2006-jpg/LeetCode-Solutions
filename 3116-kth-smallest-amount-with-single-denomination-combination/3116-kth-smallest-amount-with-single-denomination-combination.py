class Solution:
    def findKthSmallest(self, coins, k):
        n = len(coins)

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def lcm(a, b):
            return a // gcd(a, b) * b

        # Store LCM of every subset
        subsets = []

        for mask in range(1, 1 << n):
            value = 1
            bits = 0

            for i in range(n):
                if mask & (1 << i):
                    bits += 1
                    value = lcm(value, coins[i])

            subsets.append((value, bits))

        # Count how many valid amounts <= x
        def count(x):
            total = 0

            for value, bits in subsets:
                if value > x:
                    continue

                if bits % 2 == 1:
                    total += x // value
                else:
                    total -= x // value

            return total

        # Binary search for kth smallest amount
        left = 1
        right = min(coins) * k

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left