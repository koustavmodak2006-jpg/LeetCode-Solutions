class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        def findGCD(large,small):
            while large % small != 0:
                large, small = small, large % small
            return small
            
        sumOdd = count = sumEven = 0
        for i in range(1,2**n+1):
            if i %2 == 0:
                sumEven+=i
            else:
                sumOdd+=i
            count+=1
            if count ==n+n:
                break
        return findGCD(sumEven,sumOdd)