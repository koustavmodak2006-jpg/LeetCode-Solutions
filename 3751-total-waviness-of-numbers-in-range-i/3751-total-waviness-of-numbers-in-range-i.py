class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        wave = 0
        for i in range(num1,num2+1):
            num = str(i)
            for j in range(1,len(num)-1):
                if (num[j] > num[j-1] and num[j] > num[j+1]) or (num[j] < num[j-1] and num[j] < num[j+1]):
                    wave += 1
        return wave