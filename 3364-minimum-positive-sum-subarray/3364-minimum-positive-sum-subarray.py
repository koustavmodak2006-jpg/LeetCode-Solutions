from typing import List
from bisect import bisect_left

class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)

        # Calculate prefix sums
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)

        # Coordinate compression
        vals = sorted(set(prefix))
        m = len(vals)

        # Fenwick Tree
        bit = [0] * (m + 1)

        def update(i, val):
            i += 1
            while i <= m:
                bit[i] += val
                i += i & -i

        def query(i):
            s = 0
            while i > 0:
                s += bit[i]
                i -= i & -i
            return s

        def kth(k):
            idx = 0
            mask = 1 << (m.bit_length() - 1)

            while mask:
                nxt = idx + mask
                if nxt <= m and bit[nxt] < k:
                    idx = nxt
                    k -= bit[nxt]
                mask >>= 1

            return idx

        ans = float('inf')

        for i in range(l, n + 1):

            # Add valid starting prefix
            update(bisect_left(vals, prefix[i-l]), 1)

            # Remove prefixes outside the window
            if i - r - 1 >= 0:
                update(bisect_left(vals, prefix[i-r-1]), -1)

            # Find largest prefix sum smaller than current
            pos = bisect_left(vals, prefix[i])
            count = query(pos)

            if count:
                idx = kth(count)
                curr = prefix[i] - vals[idx]
                ans = min(ans, curr)

        return ans if ans != float('inf') else -1