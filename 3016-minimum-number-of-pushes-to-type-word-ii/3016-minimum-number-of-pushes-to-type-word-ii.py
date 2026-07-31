class Solution:
    def minimumPushes(self, word: str) -> int:
        letter = sorted(Counter(word).values(), reverse=True)
        res = 0

        for i,freq in enumerate(letter):
            res += (i//8 +1) *freq
        return res