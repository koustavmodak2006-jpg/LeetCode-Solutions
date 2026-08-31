# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev = head
        curr = head.next

        first = -1
        last = -1

        min_dist = float("inf")
        max_dist = -1

        pos = 1

        while curr.next:
            # Critical point:
            # local maximum OR local minimum
            if (curr.val > prev.val and curr.val > curr.next.val) or \
               (curr.val < prev.val and curr.val < curr.next.val):

                if first == -1:
                    # First critical point
                    first = pos
                else:
                    # Distance from previous critical point
                    min_dist = min(min_dist, pos - last)

                    # Distance from first critical point
                    max_dist = pos - first

                last = pos

            prev = curr
            curr = curr.next
            pos += 1

        if first == -1 or first == last:
            return [-1, -1]

        return [min_dist, max_dist]