class Solution:
    def judgeCircle(self, moves: str) -> bool:
        yAxis = {"U":1,
                "D":-1,}
        xAxis = {"R":1,
                "L":-1,}
        x_val = y_val = 0
        for i in moves:
            if i in yAxis:
                y_val+=yAxis[i]
            else:
                x_val += xAxis[i]
        return x_val == 0 and y_val == 0