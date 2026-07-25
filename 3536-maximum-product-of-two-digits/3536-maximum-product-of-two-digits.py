class Solution:
    def maxProduct(self, n: int) -> int:
        list_num = list(str(n))
        two_num = []
        res = 1
        for _ in range(2):
            i = max(list_num)
            two_num.append(i)
            list_num.remove(i)
            res *= int(i)
        return res