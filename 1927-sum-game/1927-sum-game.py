class Solution:
    def sumGame(self, num: str) -> bool:
        leftKnown = rightKnown = 0
        leftQn = rightQn = 0

        n = len(num)

        for i in range(n):
            if num[i] == "?":
                if i < n / 2:
                    leftQn += 1
                else:
                    rightQn += 1
            else:
                if i < n / 2:
                    leftKnown += int(num[i])
                else:
                    rightKnown += int(num[i])

        totalQn = leftQn + rightQn

        # Odd number of ? means Alice can always win
        if totalQn % 2 == 1:
            return True

        LEFT = leftKnown * 2 + leftQn * 9
        RIGHT = rightKnown * 2 + rightQn * 9

        if LEFT == RIGHT:
            return False

        return True