import math as m
class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        max_len = 0
        for i in range(n):
            product = 1
            lcm = 1
            gcd = 0
            for j in range(i, n):
                product *= nums[j]
                lcm = m.lcm(lcm, nums[j])
                gcd = m.gcd(gcd, nums[j])
                if product == lcm * gcd:
                    max_len = max(max_len, j - i + 1)
        return max_len