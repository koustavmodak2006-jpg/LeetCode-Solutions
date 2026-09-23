class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        minimum = prices[0]
        maximum = 0

        for price in prices:
            minimum = min(minimum, price)
            maximum = max(maximum, price - minimum)

        return maximum