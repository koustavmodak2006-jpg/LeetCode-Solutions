class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        res = {}
        for i in words:
            for j in i:
                res[j] = weights[ord(j)-97]

        value = ""
        for i in words:
            temp = 0
            for j in i:
                temp += res[j]
            temp %= 26
            value+=chr(122-temp)

        return value