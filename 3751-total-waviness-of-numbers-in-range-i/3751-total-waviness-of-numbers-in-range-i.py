class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        wave = 0
        for i in range(num1,num2+1):
            num = str(i)
            for j in range(len(num)):
                if j > 0 and j < len(num)-1 and num[j-1] < num[j] and num[j+1] < num[j]:
                    wave +=1
                elif j > 0 and j < len(num)-1 and num[j-1] > num[j] and num[j+1] > num[j]:
                    wave +=1
        return wave