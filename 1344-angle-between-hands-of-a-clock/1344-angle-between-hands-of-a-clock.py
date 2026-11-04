class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour = 0 if hour == 12 else hour*30
        hour += minutes * 0.5
        minutes = minutes*6
        return min(abs(hour-minutes),360-abs(hour-minutes))