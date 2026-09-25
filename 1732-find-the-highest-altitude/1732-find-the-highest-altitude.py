class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        res = []
        for i in range(len(gain)):
            if i == 0:
                res.append(0)
            else:
                res.append(gain[i-1]+res[i-1])
        res.append(gain[-1]+res[-1])
        return max(res)