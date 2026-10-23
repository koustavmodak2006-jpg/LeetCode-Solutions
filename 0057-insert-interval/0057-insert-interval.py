class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        intervals.append(newInterval)
        intervals.sort()

        mini = maxi = None
        res = []

        for i in intervals:
            if mini is None or maxi < i[0]:
                mini = i[0]
                maxi = i[1]
            else:
                maxi = max(maxi,i[1])
                res.pop()

            res.append([mini,maxi])

        return res