class Solution:
    def stoneGameIX(self, stones: list[int]) -> bool:
        cnt = [0, 0, 0]

        for stone in stones:
            cnt[stone % 3] += 1

        # If there are no stones with remainder 1 or 2,
        # Alice cannot make a winning move.
        if cnt[1] == 0 and cnt[2] == 0:
            return False

        # If cnt[0] is even, the 0-mod-3 stones effectively
        # don't change whose turn it is.
        if cnt[0] % 2 == 0:
            return cnt[1] > 0 and cnt[2] > 0

        # If cnt[0] is odd, Alice can win if one side
        # has at least two more stones than the other.
        return abs(cnt[1] - cnt[2]) > 2