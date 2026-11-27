class Solution:
    def canAliceWin(self, n: int) -> bool:
        alice = 10
        while n > 0:
            if n>=alice:
                n-=alice
                alice-=1
            else:
                return False
            bob = alice
            if n>=bob:
                n-=bob
                bob-=1
            else:
                return True
            alice=bob
        else:
            return False