class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ""
        for i in range(len(digits)):
            num += str(digits[i])
        print(num)
        num = str(int(num) + 1)
        res = []
        for i in num:
            res.append(int(i))
        return res