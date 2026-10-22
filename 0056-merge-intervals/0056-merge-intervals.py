class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals = sorted(intervals)
        res = []
        mini = maxi = None
        for i in intervals:
            if mini == None or maxi == None:
                mini = i[0]
                maxi = i[1]
                res.append([mini,maxi])

            elif mini <= i[0] <= maxi:
                maxi = max(maxi,i[1])
                res.pop()
                res.append([mini, maxi])
            else:
                res.append([i[0],i[1]])
                mini = i[0]
                maxi = i[1]
        return res