class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n >0:
            for x in range(0,31):
                if 2 ** x == n:
                    return True
        else:
            for x in range(-31,0):
                if 2 ** x == n:
                    return True
        return False
