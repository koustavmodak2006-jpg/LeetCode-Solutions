class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1, y1, x2, y2 = rec1
        a1, b1, a2, b2 = rec2

        # Check if there is a positive-width overlap
        overlap_width = min(x2, a2) - max(x1, a1)

        # Check if there is a positive-height overlap
        overlap_height = min(y2, b2) - max(y1, b1)

        return overlap_width > 0 and overlap_height > 0