class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        large = n*(n + 1)
        small = n * n

        while large % small != 0:
            large, small = small, large % small
        return small