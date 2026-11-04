class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour = 0+minutes * 0.5 if hour == 12 else (hour * 30)+minutes * 0.5

        return min(abs(hour - minutes*6), 360 - abs(hour - minutes*6))