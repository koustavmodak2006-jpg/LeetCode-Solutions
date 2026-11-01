# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next:
            return None

        slow = fast = head
        temp = None

        while fast and fast.next:
            temp = slow
            fast = fast.next.next
            slow = slow.next
        temp.next = slow.next
        return head