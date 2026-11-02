class Solution:
    def processStr(self, s: str) -> str:
        res = []
        for i in s:
            if i == "#":
                res.extend(res)
            elif i == "%":
                res.reverse()
            elif i == "*" and res:
                res.pop()
            elif "a"<=i<="z":
                res.append(i)
            else:
                continue
        return "".join(res)