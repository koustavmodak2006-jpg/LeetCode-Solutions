class Solution:
    def simplifyPath(self, path: str) -> str:
        res = []
        directory = path.split("/")

        for i in directory:
            if not i or i == ".":
                continue

            elif i == "..":
                if res:
                    res.pop()

            else:
                res.append(i)

        return "/" + "/".join(res)