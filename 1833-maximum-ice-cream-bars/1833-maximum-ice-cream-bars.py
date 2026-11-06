class Solution:
    def maxIceCream(self, costs: list[int], coins: int) -> int:
        costs.sort()
        count = res = 0
        for i in costs:
            if res+i <= coins:
                res += i
                count +=1
        return count