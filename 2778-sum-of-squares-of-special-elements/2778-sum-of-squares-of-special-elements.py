class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        for i, num in enumerate(nums, start=1):
            print(i,num)
            if n % i == 0:
                total += num ** 2
        return total