from collections import Counter

FACTOR_COUNTS = {
    0: Counter(),
    1: Counter(),
    2: Counter([2]),
    3: Counter([3]),
    4: Counter([2, 2]),
    5: Counter([5]),
    6: Counter([2, 3]),
    7: Counter([7]),
    8: Counter([2, 2, 2]),
    9: Counter([3, 3]),
}

class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        primeCount, ok = self.getPrimeCount(t)
        if not ok:
            return "-1"

        factorCount = self.getFactorCount(primeCount)
        if sum(factorCount.values()) > len(num):
            return "".join(d * c for d, c in factorCount.items())

        primePrefix = Counter()
        for ch in num:
            primePrefix += FACTOR_COUNTS[int(ch)]

        firstZero = num.find("0")
        if firstZero == -1:
            firstZero = len(num)

        if firstZero == len(num) and primeCount <= primePrefix:
            return num

        for i in range(len(num) - 1, -1, -1):
            d = int(num[i])
            primePrefix -= FACTOR_COUNTS[d]

            space = len(num) - 1 - i

            if i <= firstZero:
                for bigger in range(d + 1, 10):
                    need = self.getFactorCount(
                        primeCount - primePrefix - FACTOR_COUNTS[bigger]
                    )

                    if sum(need.values()) <= space:
                        ones = space - sum(need.values())
                        return (
                            num[:i]
                            + str(bigger)
                            + "1" * ones
                            + "".join(k * v for k, v in need.items())
                        )

        factorCount = self.getFactorCount(primeCount)

        return (
            "1" * (len(num) + 1 - sum(factorCount.values()))
            + "".join(d * c for d, c in factorCount.items())
        )

    def getPrimeCount(self, t):
        cnt = Counter({2: 0, 3: 0, 5: 0, 7: 0})

        for p in (2, 3, 5, 7):
            while t % p == 0:
                t //= p
                cnt[p] += 1

        return cnt, t == 1

    def getFactorCount(self, cnt):
        c8 = cnt[2] // 3
        rem2 = cnt[2] % 3

        c9 = cnt[3] // 2
        c3 = cnt[3] % 2

        c4 = rem2 // 2
        c2 = rem2 % 2

        c6 = 0

        if c2 and c3:
            c2 = 0
            c3 = 0
            c6 = 1

        if c3 and c4:
            c2 = 1
            c6 = 1
            c3 = 0
            c4 = 0

        return {
            "2": c2,
            "3": c3,
            "4": c4,
            "5": cnt[5],
            "6": c6,
            "7": cnt[7],
            "8": c8,
            "9": c9,
        }